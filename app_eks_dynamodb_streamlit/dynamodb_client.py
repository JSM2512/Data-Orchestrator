import boto3
from boto3.dynamodb.conditions import Attr
from decimal import Decimal
from typing import Dict, List, Any

class DynamoDBClient:
    def __init__(self, config):
        self.config = config
        self.dynamodb = boto3.resource(
            'dynamodb',
            region_name=config.AWS_REGION,
            aws_access_key_id=config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY
        )
        self.table = self.dynamodb.Table(config.DYNAMODB_TABLE_NAME)
    
    def query_data(self, query_params: Dict) -> List[Dict]:
        """
        Query data from DynamoDB based on parameters matching selected.csv column names.
        Supports filtering by passenger_count, tip_amount, fare_amount, trip_distance, VendorID, payment_type, tpep_pickup_datetime.
        Column types:
            - passenger_count: string
            - tip_amount: string
            - fare_amount: string
            - trip_distance: string
            - VendorID: string
            - payment_type: string
            - tpep_pickup_datetime: string
        """
        try:
            filter_expression = None

            # Passenger count filter (stored as string)
            if query_params.get('passenger_count_min') is not None:
                filter_expr = Attr('passenger_count').gte(str(query_params['passenger_count_min']))
                filter_expression = filter_expr if filter_expression is None else filter_expression & filter_expr

            # Tip amount filter (stored as string)
            if query_params.get('tip_amount_min') is not None:
                filter_expr = Attr('tip_amount').gte(str(query_params['tip_amount_min']))
                filter_expression = filter_expr if filter_expression is None else filter_expression & filter_expr

            # Fare amount range filter (stored as string)
            if query_params.get('fare_amount_range'):
                min_fare, max_fare = query_params['fare_amount_range']
                filter_expr = Attr('fare_amount').between(str(min_fare), str(max_fare))
                filter_expression = filter_expr if filter_expression is None else filter_expression & filter_expr

            # Trip distance range filter (stored as string)
            if query_params.get('trip_distance_range'):
                min_dist, max_dist = query_params['trip_distance_range']
                filter_expr = Attr('trip_distance').between(str(min_dist), str(max_dist))
                filter_expression = filter_expr if filter_expression is None else filter_expression & filter_expr

            # VendorID filter (stored as string)
            if query_params.get('VendorID'):
                filter_expr = Attr('VendorID').eq(str(query_params['VendorID']))
                filter_expression = filter_expr if filter_expression is None else filter_expression & filter_expr

            # Payment type filter (stored as string)
            if query_params.get('payment_type'):
                filter_expr = Attr('payment_type').eq(str(query_params['payment_type']))
                filter_expression = filter_expr if filter_expression is None else filter_expression & filter_expr

            # Date range filter (tpep_pickup_datetime, stored as string)
            if query_params.get('date_range'):
                date_range = query_params['date_range']
                if len(date_range) == 2:
                    start_date, end_date = date_range
                    filter_expr = Attr('tpep_pickup_datetime').between(start_date, end_date)
                    filter_expression = filter_expr if filter_expression is None else filter_expression & filter_expr

            scan_kwargs = {}
            if filter_expression is not None:
                scan_kwargs['FilterExpression'] = filter_expression

            response = self.table.scan(**scan_kwargs)
            items = self._convert_decimals(response.get('Items', []))

            return items[:100]  # Limit results for performance

        except Exception as e:
            print(f"Error querying DynamoDB: {str(e)}")
            return []

    def _convert_decimals(self, obj):
        """
        Recursively convert Decimal objects to float for JSON serialization.
        This will also handle string values, leaving them untouched.
        """
        if isinstance(obj, list):
            return [self._convert_decimals(item) for item in obj]
        elif isinstance(obj, dict):
            return {key: self._convert_decimals(value) for key, value in obj.items()}
        elif isinstance(obj, Decimal):
            return float(obj)
        else:
            return obj

    def health_check(self) -> bool:
        """
        Check if DynamoDB table connection is healthy.
        """
        try:
            status = self.table.table_status
            return True
        except Exception:
            return False
    #         scan_kwargs = {}
    #         if filter_expression is not None:
    #             scan_kwargs['FilterExpression'] = filter_expression

    #         items = []
    #         response = self.table.scan(**scan_kwargs)
    #         items.extend(self._convert_decimals(response.get('Items', [])))

    #         # Handle pagination: get all items
    #         while 'LastEvaluatedKey' in response:
    #             scan_kwargs['ExclusiveStartKey'] = response['LastEvaluatedKey']
    #             response = self.table.scan(**scan_kwargs)
    #             items.extend(self._convert_decimals(response.get('Items', [])))

    #         return items  # No slicing, return all

    #     except Exception as e:
    #         print(f"Error querying DynamoDB: {str(e)}")
    #         return []

    # def _convert_decimals(self, obj):
    #     # [unchanged]
    #     if isinstance(obj, list):
    #         return [self._convert_decimals(item) for item in obj]
    #     elif isinstance(obj, dict):
    #         return {key: self._convert_decimals(value) for key, value in obj.items()}
    #     elif isinstance(obj, Decimal):
    #         return float(obj)
    #     else:
    #         return obj

    # def health_check(self) -> bool:
    #     try:
    #         status = self.table.table_status
    #         return True
    #     except Exception:
    #         return False
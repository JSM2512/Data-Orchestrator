from dynamodb_client import DynamoDBClient
import config
import boto3
from decimal import Decimal

# Initialize config and client
config = config.Config()
dynamodb_client = DynamoDBClient(config)

def convert_floats_to_decimal(record):
    for k, v in record.items():
        # If the value is a float, convert to Decimal
        if isinstance(v, float):
            record[k] = Decimal(str(v))
        # If the value is a string that looks like a float, convert to Decimal
        elif isinstance(v, str):
            try:
                float_val = float(v)
                # Only convert if string is a number
                record[k] = Decimal(v)
            except ValueError:
                pass  # leave as string
        # Fix VendorID to always be string
        if "VendorID" in record:
            record["VendorID"] = str(record["VendorID"])
    return record

def add_trip(record):
    dynamodb = boto3.resource('dynamodb',region_name='us-east-1')
    table = dynamodb.Table('TaxiTripData')
    table.put_item(Item=record)

def query_trips_by_passenger_and_tip(passenger_count_min, tip_amount_min, limit=100):
    """
    Query DynamoDB for trips with passenger_count >= passenger_count_min
    and tip_amount >= tip_amount_min.
    Returns up to 'limit' results.
    """
    query_params = {
        'passenger_count_min': passenger_count_min,
        'tip_amount_min': tip_amount_min
    }
    results = dynamodb_client.query_data(query_params)
    return results[:limit]

def query_trips(filters, limit=100):
    """
    General query function for advanced filters.
    'filters' is a dict that can include:
        - passenger_count_min
        - tip_amount_min
        - fare_amount_range (tuple)
        - trip_distance_range (tuple)
        - date_range (list of str)
    """
    results = dynamodb_client.query_data(filters)
    return results[:limit]
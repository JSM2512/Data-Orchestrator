from dynamodb_client import DynamoDBClient
import config

# Initialize config and client
config = config.Config()
dynamodb_client = DynamoDBClient(config)

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
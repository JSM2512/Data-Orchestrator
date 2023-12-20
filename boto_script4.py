import os

import boto3
import pandas as pd
from boto3.s3.transfer import TransferConfig


def download_s3_csv(bucket_name, key, local_path):
    s3_client = boto3.client('s3', aws_access_key_id='AKIA2VRUPJ2Z6CYUN55V',
                             aws_secret_access_key='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', region_name='us-east-2')

    # Download the file from S3 to the local path
    s3_client.download_file(bucket_name, key, local_path, Config=TransferConfig(max_concurrency=10,use_threads=True))


def read_local_csv(local_path):
    # Read CSV into a Pandas DataFrame
    dataset = pd.read_csv(local_path)
    return dataset

def run_sql_query(df, query):
    # Run SQL query on the DataFrame
    result = df.query(query)
    return result

def main():
    bucket_name = 'dsdproject1'
    key = 'yellow_tripdata_2015-02.csv'
    local_path = 'test/yellow_tripdata_2016-02.csv'  # Local path to save the downloaded file

    if not os.path.exists(local_path):
        download_s3_csv(bucket_name, key, local_path)

    df = read_local_csv(local_path)

    # Rest of your code...
    print("Original DataFrame:")
    print(df)

    query1 = "passenger_count > 1"
    result = run_sql_query(df, query1)

    print("\nResult of Query:")
    print(result[['passenger_count']])

    query2 = "tip_amount > 2"
    result = run_sql_query(df, query2)

    print("\nResult of Query:")
    print(result[['tip_amount']])

if __name__ == "__main__":
    main()

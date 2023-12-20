# import os
# import boto3
# import pandas as pd
# from boto3.s3.transfer import TransferConfig
#
# def read_csv_generator(file_path, chunksize=10000):
#     for chunk in pd.read_csv(file_path, chunksize=chunksize):
#         yield chunk
#
# def download_s3_csv(bucket_name, key, local_path):
#     s3_client = boto3.client(
#         's3',
#         aws_access_key_id='AKIA2VRUPJ2Z6CYUN55V',
#         aws_secret_access_key='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',
#         region_name='us-east-2'
#     )
#
#     try:
#         # Download the file from S3 to the local path
#         s3_client.download_file(
#             bucket_name,
#             key,
#             local_path,
#             Config=TransferConfig(max_concurrency=10, use_threads=True)
#         )
#     finally:
#         # Close the S3 client explicitly to free up resources
#         s3_client.meta.client.close()
#
# def run_sql_query(df, query):
#     # Run SQL query on the DataFrame inplace
#     df.query(query, inplace=True)
#
# def main():
#     bucket_name = 'dsdproject1'
#     key = 'yellow_tripdata_2015-01.csv'
#     local_path = 'D:\\archive\\test\\yellow_tripdata_2015-01.csv'  # Local path to save the downloaded file
#
#     if not os.path.exists(local_path):
#         print("Downloading file...")
#         download_s3_csv(bucket_name, key, local_path)
#
#     print("data")
#     # Use a generator for reading the CSV file
#     dataset_generator = read_csv_generator(local_path)
#
#     # Initialize DataFrame with the first chunk
#     df = next(dataset_generator)
#
#     # Iterate over remaining chunks and concatenate to the DataFrame
#     for chunk in dataset_generator:
#         df = pd.concat([df, chunk], ignore_index=True)
#
#     # Rest of your code...
#     print("Original DataFrame:")
#     print(df)
#
#     query1 = "passenger_count > 1"
#     run_sql_query(df, query1)
#     print("\nResult of Query:")
#     print(df[['passenger_count']])
#
#     query2 = "tip_amount > 2"
#     run_sql_query(df, query2)
#     print("\nResult of Query:")
#     print(df[['tip_amount']])
#
# if __name__ == "__main__":
#     main()









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
    key = 'yellow_tripdata_2015-01.csv'
    local_path = 'test/yellow_tripdata_2015-01.csv'  # Local path to save the downloaded file

    if not os.path.exists(local_path):
        download_s3_csv(bucket_name, key, local_path)

        # Load only necessary columns to conserve memory
    columns_to_load = ['passenger_count', 'tip_amount']
    df = pd.read_csv(local_path, nrows=100,usecols=columns_to_load)

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

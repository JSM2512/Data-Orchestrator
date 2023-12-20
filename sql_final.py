import pandas as pd

def main():

    csv_file_path_1 = 'mount_s3/yellow_tripdata_2015-01.csv'
    csv_file_path_2 = 'mount_s3/yellow_tripdata_2015-02.csv'
    csv_file_path_3 = 'mount_s3/yellow_tripdata_2016-01.csv'
    csv_file_path_4 = 'mount_s3/yellow_tripdata_2016-02.csv'

    print("DATASET-1:")
    df1 = pd.read_csv(csv_file_path_1)

    print("Original DataFrame:")
    print(df1)

    query1 = "passenger_count > 1"
    result = run_sql_query(df1, query1)

    print("\nResult of Query for data-1:")
    print(result[['passenger_count']])

    print("DATASET-2:")
    df2 = pd.read_csv(csv_file_path_2)

    print("Original DataFrame:")
    print(df2)

    query2 = "passenger_count > 1"
    result = run_sql_query(df2, query2)

    print("\nResult of Query for data-2:")
    print(result[['passenger_count']])

    print("DATASET-3:")
    df3 = pd.read_csv(csv_file_path_3)

    print("Original DataFrame:")
    print(df3)

    query3 = "passenger_count > 1"
    result = run_sql_query(df3, query3)

    print("\nResult of Query for data-3:")
    print(result[['passenger_count']])

    print("DATASET-4:")
    df4 = pd.read_csv(csv_file_path_4)

    print("Original DataFrame:")
    print(df4)

    query4 = "passenger_count > 1"
    result = run_sql_query(df4, query4)

    print("\nResult of Query for data-4:")
    print(result[['passenger_count']])



    # query2 = "tip_amount > 2"
    # result = run_sql_query(df, query2)
    #
    # print("\nResult of Query:")
    # print(result[['tip_amount']])



def run_sql_query(df, query):
    # Run SQL query on the DataFrame
    result = df.query(query)
    return result

if __name__ == "__main__":
    main()


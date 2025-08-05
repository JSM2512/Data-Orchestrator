import pandas as pd

def main():
    # Replace 'your_file.csv' with the actual path to your CSV file
    csv_file_path = 'mount_s3/yellow_tripdata_2016-01.csv'

    # Read CSV into a Pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Display the DataFrame
    print("Original DataFrame:")
    print(df)

    # SQL query to filter data
    query1 = "passenger_count > 1"
    result = run_sql_query(df, query1)

    print("\nResult of Query:")
    print(result[['passenger_count']])

    query2 = "tip_amount > 2"
    result = run_sql_query(df, query2)

    print("\nResult of Query:")
    print(result[['tip_amount']])



def run_sql_query(df, query):
    # Run SQL query on the DataFrame
    result = df.query(query)
    return result

if __name__ == "__main__":
    main()


import streamlit as st
import pandas as pd
import dynamodb_utils as ut

st.title("🚕 NYC Taxi Trip Data Explorer")

passenger_count = st.number_input("Passenger Count", min_value=1, max_value=10, value=2)
min_tip = st.number_input("Minimum Tip Amount", min_value=0.0, value=2.0)
vendor_id = st.selectbox("Vendor", options=["1", "2"])
payment_type = st.selectbox("Payment Type", options=["1. Credit card", "2. Cash"])
min_distance = st.number_input("Min Trip Distance (miles)", min_value=0.0, value=0.0)
max_distance = st.number_input("Max Trip Distance (miles)", min_value=0.0, value=10.0)
# date_range = st.date_input("Pickup Date Range", [])

filters = {
    "passenger_count_min": passenger_count,
    "tip_amount_min": min_tip,
    "VendorID": vendor_id,
    "payment_type": payment_type[0:1:1],
    "trip_distance_range": (min_distance, max_distance)
}


if st.button("Query DynamoDB"):
    items = ut.query_trips(filters)
    if items:
        df = pd.DataFrame(items)
        st.dataframe(df)
        st.write("Total Trips:", len(df))
        # If you already have a DataFrame called df:
        df['fare_amount'] = pd.to_numeric(df['fare_amount'], errors='coerce')
        df['tip_amount'] = pd.to_numeric(df['tip_amount'], errors='coerce')
        st.write("Average Fare:", df['fare_amount'].mean())
        st.write("Total Tip:", df['tip_amount'].sum())
        # Add charts here, e.g., st.bar_chart(df['fare_amount'])
    else:
        st.warning("No data found for the given filters.")
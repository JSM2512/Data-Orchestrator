import streamlit as st
import pandas as pd
import dynamodb_utils as ut

st.title("🚕 NYC Taxi Trip Data Platform")

tab1, tab2 = st.tabs(["Query Trips", "Add New Trip"])

with tab1:
    st.header("Query DynamoDB")
    passenger_count = st.number_input("Passenger Count", min_value=1, max_value=10, value=2)
    min_tip = st.number_input("Minimum Tip Amount", min_value=0.0, value=2.0)
    vendor_id = st.selectbox("Vendor", options=["1", "2"])
    payment_type = st.selectbox("Payment Type", options=["1. Credit card", "2. Cash"])
    min_distance = st.number_input("Min Trip Distance (miles)", min_value=0.0, value=0.0)
    max_distance = st.number_input("Max Trip Distance (miles)", min_value=0.0, value=10.0)

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
            df['fare_amount'] = pd.to_numeric(df['fare_amount'], errors='coerce')
            df['tip_amount'] = pd.to_numeric(df['tip_amount'], errors='coerce')
            st.write("Average Fare:", df['fare_amount'].mean())
            st.write("Total Tip:", df['tip_amount'].sum())
        else:
            st.warning("No data found for the given filters.")

with tab2:
    st.header("Add New Trip Record")
    with st.form("Ingest New Trip"):
        trip_id = st.text_input("Trip ID")
        passenger_count_in = st.number_input("Passenger Count", min_value=1, max_value=10, value=1)
        fare_amount = st.text_input("Fare Amount")
        tip_amount = st.text_input("Tip Amount")
        trip_distance = st.text_input("Trip Distance")
        vendor_id_in = st.selectbox("Vendor ID", options=["1", "2"])
        payment_type_in = st.selectbox("Payment Type", options=["1", "2"])
        pickup_datetime = st.text_input("Pickup Datetime (YYYY-MM-DD HH:MM:SS)")
        submitted = st.form_submit_button("Add Trip")

        if submitted:
            new_record = {
                "trip_id": trip_id,
                "passenger_count": str(passenger_count_in),
                "fare_amount": fare_amount,
                "tip_amount": tip_amount,
                "trip_distance": trip_distance,
                "VendorID": vendor_id_in,
                "payment_type": payment_type_in,
                "tpep_pickup_datetime": pickup_datetime,
            }
            ut.add_trip(new_record)  # Write to DynamoDB, implement in dynamodb_utils.py
            st.success("Trip record uploaded!")

import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title("Groundwater Level Prediction – ML Model")

st.write("Upload datasets and run the model to see predictions.")

# Upload CSVs
water_csv = st.file_uploader("Upload WaterLevel.csv", type=["csv"])
well_csv = st.file_uploader("Upload welldata.csv", type=["csv"])

if water_csv and well_csv:
    water_df = pd.read_csv(water_csv)
    well_df = pd.read_csv(well_csv)

    st.subheader("Preview of Water Level Data")
    st.dataframe(water_df.head())

    st.subheader("Preview of Well Data")
    st.dataframe(well_df.head())

    # When user clicks "Run Model"
    if st.button("Run Prediction"):
        st.write("Running Machine Learning Model...")
        
        # ---- YOUR main.py CODE GOES HERE ----
        
        # Prediction Example
        st.success("Prediction Completed!")
        st.line_chart(np.random.randn(20))

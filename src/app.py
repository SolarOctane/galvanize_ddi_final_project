import streamlit as st
import pandas as pd
import joblib
import pickle

# Load the model
@st.cache_resource
def load_model():
    model = joblib.load('random_forest_regressor_model_V1.pkl')
    return model

model = load_model()

# Title of the app
st.title("Encounter Count Prediction")

# Load the data
data = pd.read_csv("nationwide-encounters-fy21-fy24-aor.csv")

# Input form
# Select values for "Citizenship"
citizenship = st.selectbox("Select Citizenship", options=data["Citizenship"].unique())

# Select values for "Demographic"
demographic = st.selectbox("Select Demographic", options=data["Demographic"].unique())

# Select values for "Encounter Type"
encounter_type = st.selectbox("Select Encounter Type", options=data["Encounter Type"].unique())

# Select values for "AOR (Abbv)"
aor = st.selectbox("Select AOR (Abbv)", options=data["AOR (Abbv)"].unique())

# Select values for "Fiscal Year"
fiscal_year = st.selectbox("Select Fiscal Year", options=data["Fiscal Year"].unique())

st.header("📥 Target Feature")

# Select "Encounter Count" as the only target variable
target_variable = "Encounter Count"
st.write(f"Target Variable: {target_variable}")


# Create a button to make predictions
if st.button("Predict"):
    # Prepare the input data for prediction
    input_data = pd.DataFrame({
        "Citizenship": [citizenship],
        "Demographic": [demographic],
        "Encounter Type": [encounter_type],
        "AOR (Abbv)": [aor],
        "Fiscal Year": [fiscal_year]  # Assuming the latest fiscal year is 2024
    })

    # Make the prediction
    prediction = model.predict(input_data)

    # Display the prediction result
    st.success(f"Predicted {target_variable}: {prediction[0]}")

# Visualize the results and do not display distribution 
st.subheader("📊 Prediction Results")
st.write("Here you can visualize the prediction results.")
st.bar_chart(prediction)

import streamlit as st

# Conversion factors
conversion_factors = {
    "Length": {
        "Meter": 1, "Kilometer": 0.001, "Mile": 0.000621371,
        "Centimeter": 100, "Millimeter": 1000, "Inch": 39.3701, "Foot": 3.28084
    },
    "Time": {
        "Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400,
    },
    "Weight": {
        "Gram": 1, "Kilogram": 0.001, "Pound": 0.00220462, "Ounce": 0.035274
    }
}

# Streamlit UI
st.title("Google Unit Converter 🌍")

# Select Category
category = st.selectbox("Select Category", list(conversion_factors.keys()))

# Select Units
unit_from = st.selectbox("From", list(conversion_factors[category].keys()))
unit_to = st.selectbox("To", list(conversion_factors[category].keys()))

# Input Value
value = st.number_input("Enter Value", min_value=0.0)

# Conversion Logic
if st.button("Convert"):
    result = value * conversion_factors[category][unit_to] / conversion_factors[category][unit_from]
    st.success(f"Converted Value: {result} {unit_to}")

import streamlit as st

def convert(value, from_unit, to_unit, category):
    conversion_factors = {
        "Length": {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371, "Feet": 3.28084},
        "Weight": {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274},
        "Temperature": {"Celsius": (lambda x: x, lambda x: x), 
        "Fahrenheit": (lambda x: x * 9/5 + 32, lambda x: (x - 32) * 5/9), 
        "Kelvin": (lambda x: x + 273.15, lambda x: x - 273.15)
        },
    }
    if category in ["Length", "Weight"]:
        result = value / conversion_factors[category][from_unit] * conversion_factors[category][to_unit]
    elif category == "Temperature":
        to_celsius = conversion_factors["Temperature"][from_unit][1]
        from_celsius = conversion_factors["Temperature"][to_unit][0]
        result = from_celsius(to_celsius(value))
    else:
        result = "Invalid Conversion"
    return result

st.title("Unit Converter")

category = st.selectbox("Select Category:", ["Length", "Weight", "Temperature"])

units = {
    "Length": ["Meters", "Kilometers", "Miles", "Feet"],
    "Weight": ["Kilograms", "Grams", "Pounds", "Ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

from_unit = st.selectbox("From:", units[category])
to_unit = st.selectbox("To:", units[category])
value = st.number_input("Enter Value:", min_value=0.0, format="%.2f")

if st.button("Convert"):
    result = convert(value, from_unit, to_unit, category)
    st.success(f"Result: {result:.2f} {to_unit}")
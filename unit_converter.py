import streamlit as st # streamlit is a library for building web apps

# function to convert units based on predefined conversion factors or formulas
def convert_units(value, unit_from, unit_to):

    conversions = {
        "meter_kilometer": 0.001, # 1 meter = 0.001 kilometer
        "kilometer_meter":1000, # 1 kilometer = 1000 meter
        "gram_kilogram": 0.001, # 1 gram = 0.001 kilogram
        "kilogram_gram": 1000 # 1 kilogram = 1000 gram
    }

    key = f"{unit_from}_{unit_to}" # generate a key based on the input and output units

    # logic to convert units
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "convertion not supported"  # Return message if conversion is not defined
    
st.title("unit converter") # set the title of web app 

#user input: numerical value to convert 
value = st.number_input("Enter the value:")

#drop to select unit to convert from
unit_from = st.selectbox("convert from:", ["meter", "kilometer", "gram", "kilogram"])

# drop down to select unit to convrt to
unit_to = st.selectbox("convert to:", ["meter", "kilometer", "gram", "kilogram"])

# button to triger the convertion
if st.button("convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"converted value: {result}")



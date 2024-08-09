import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for the two numbers
num1 = st.number_input("Enter first number", value=0.0, format="%.2f")
num2 = st.number_input("Enter second number", value=0.0, format="%.2f")

# Dropdown for selecting operation
operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform the calculation
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    result = num1 / num2 if num2 != 0 else "Cannot divide by zero"

# Display the result
st.write("Result:", result)

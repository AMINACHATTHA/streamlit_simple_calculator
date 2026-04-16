import streamlit as st
import math

st.title("🧮 Simple Calculator")

# Operation selection
operation = st.selectbox(
    "Choose Operation",
    ("Add", "Subtract", "Multiply", "Divide", "Square Root", "Power", "Logarithm")
)

# Input fields
if operation in ["Add", "Subtract", "Multiply", "Divide", "Power"]:
    num1 = st.number_input("Enter first number")
    num2 = st.number_input("Enter second number")

elif operation in ["Square Root", "Logarithm"]:
    num1 = st.number_input("Enter number")

# Calculate button
if st.button("Calculate"):

    if operation == "Add":
        result = num1 + num2

    elif operation == "Subtract":
        result = num1 - num2

    elif operation == "Multiply":
        result = num1 * num2

    elif operation == "Divide":
        if num2 == 0:
            result = "Error! Division by zero"
        else:
            result = num1 / num2

    elif operation == "Square Root":
        if num1 < 0:
            result = "Error! Negative number"
        else:
            result = math.sqrt(num1)

    elif operation == "Power":
        result = math.pow(num1, num2)

    elif operation == "Logarithm":
        if num1 <= 0:
            result = "Error! Log undefined"
        else:
            result = math.log(num1)

    st.success(f"Result: {result}")
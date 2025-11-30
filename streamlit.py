import streamlit as st

st.title("🧮 Simple Calculator")

# Input numbers
num1 = st.number_input("Enter first number:", format="%.2f")
num2 = st.number_input("Enter second number:", format="%.2f")

# Select operation
operation = st.selectbox("Select Operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate on button click
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    else:  # Divide
        if num2 == 0:
            st.error("❌ Cannot divide by zero!")
            result = None
        else:
            result = num1 / num2

    if result is not None:
        st.success(f"Result: **{result}**")

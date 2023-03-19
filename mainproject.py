import streamlit
import streamlit as st
st.title("BMI Calculator")
st.subheader("Enter your personal details and calculate your BMI")
name = st.text_input("Name")
gender = st.radio("Gender", ["Male", "Female", "Other"])
age = st.number_input("Age", min_value=0, max_value=120)
address = st.text_input("Address")
hobbies = st.multiselect("Hobbies", ["Reading", "Gaming", "Sports", "Music"])
weight = st.number_input("Weight in kg", min_value=0.0, max_value=500.0, step=0.1)
height = st.number_input("Height in cms", min_value=0, max_value=300)
if st.button("Calculate BMI"):
    bmi = weight / ((height / 100) ** 2)
    st.write(f"Your BMI is {bmi:.2f}")

import streamlit as st

# Title of the App
st.title("Growth Mindset Challenge - Streamlit Web App")

# Introduction
st.write("### What is a Growth Mindset?")
st.write("A growth mindset means believing in the ability to improve through effort, learning, and perseverance.")

# User Input Section
name = st.text_input("Enter your name:", "")

if name:
    st.write(f"Welcome, {name}! Ready to adopt a growth mindset? 🚀")

# Challenge Question
if st.button("Take the Challenge"):
    st.write("Great! Start working on your project now and submit it ASAP.")

# Footer
st.write("Made with using Streamlit.")

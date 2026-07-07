import streamlit as st
import pandas as pd
import time

# ==================================================
# STREAMLIT BASICS
# ==================================================

st.title("Learning Streamlit")
st.header("I am Learning Streamlit")
st.subheader("Exploring Different Streamlit Components")

st.write("This is a normal text.")

# ==================================================
# TEXT ELEMENTS
# ==================================================

st.header("Text Elements")

st.markdown("""
### My Favourite Foods
- Burger
- Pizza
- Chowmin
- Vada Pav
""")

st.code("""
def foo(input):
    return input**2

x = foo(2)
""")

st.latex(r'x^2 + y^2 + 2 = 0')

# ==================================================
# DATA DISPLAY
# ==================================================

st.header("Data Display")

df = pd.DataFrame({
    'name': ['Anushka', 'Ram', 'Kunj'],
    'marks': [50, 60, 70],
    'package': [90, 50, 90]
})

st.dataframe(df)
st.metric("Revenue", "Rs 3L", "-3%")

st.json({
    'name': ['Anushka', 'Ram', 'Kunj'],
    'marks': [50, 60, 70],
    'package': [90, 50, 90]
})

# ==================================================
# MEDIA ELEMENTS
# ==================================================

st.header("Media Elements")

st.image("media/cat.jpeg")
st.video("media/anushki.mp4")

# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("Sidebar")

# ==================================================
# COLUMNS LAYOUT
# ==================================================

st.header("Columns Layout")

col1, col2 = st.columns(2)

with col1:
    st.image("media/cat.jpeg")

with col2:
    st.video("media/anushki.mp4")

# ==================================================
# ALERT MESSAGES
# ==================================================

st.header("Alert Messages")

st.error("Login Failed")
st.success("Login Successful!")
st.info("Normal Information")
st.warning("Warning!")

# ==================================================
# PROGRESS BAR
# ==================================================

st.header("Progress Bar")

bar = st.progress(0)

for i in range(1, 101):
    time.sleep(0.05)
    bar.progress(i)

# ==================================================
# INPUT WIDGETS
# ==================================================

st.header("Input Widgets")

email = st.text_input("Enter Email")
number = st.number_input("Enter Number")
date = st.date_input("Enter Registration Date")

# ==================================================
# LOGIN FORM
# ==================================================

st.header("Login Demo")

email = st.text_input("Login Email")
password = st.text_input("Enter Password", type="password")
gender = st.selectbox("Select Gender", ["Male", "Female", "Others"])

btn = st.button("Login")

if btn:
    if email == "codeanushka@gmail.com" and password == "1234":
        st.success("Login Successful")
        st.balloons()
        st.write("Selected Gender:", gender)
    else:
        st.error("Login Failed")

# ==================================================
# FILE UPLOADER
# ==================================================

st.header("CSV File Uploader")

file = st.file_uploader("Upload a CSV File")

if file is not None:
    df = pd.read_csv(file)
    st.subheader("Statistical Summary")
    st.dataframe(df.describe())
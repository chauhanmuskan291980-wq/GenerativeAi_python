import streamlit as st
import pandas as pd
st.title("Streamlit Text Input")

name = st.text_input("Enter your name:")

age=st.slider("Select Your age:",0,100,25)

st.write(f"Your age is {age}.")

options = ["pyhton","Javascript","c++","Java"]
chioce = st.selectbox("Choose your favorite language:",options)
st.write(f"You selected {chioce}")


if name:
    st.write(f"Hello {name}")


data = {
    "Name":['Johne',"Muskan","Jake","jill"],
    "Age":[23,34,45,67],
    "City":["New York","Los Angeles","Chicago","Houston"]
}

df = pd.DataFrame(data)
st.write(df)

uploaded_file =st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

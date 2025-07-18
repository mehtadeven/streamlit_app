import streamlit as st
import pandas as pd
from PIL import Image

# Want to make a Currency Calculator App load a data from csv file
im = Image.open("Money.png")
st.set_page_config(
    page_title="Currency Calculator App",
    page_icon=im,
    layout="wide",
)

st.title("Currency Converter App 💵")

file =  st.file_uploader("Upload you csv file" ,type=["csv"])

if file:
  df = pd.read_csv(file)
  # Now want to take a input from user
  amount = st.number_input(("Enter the amount"), 1)
  st.write(f"You want to convert {amount} Dollar rupees")
  st.dataframe(df)
  selected_currency = st.selectbox("Select the currency",df["Currency"])
  currency_rate = df.loc[df["Currency"] == selected_currency, "Value in INR (Approx.)"].values[0]
  converted_amount = amount * currency_rate
  st.write(f"You will get {converted_amount} rupees")

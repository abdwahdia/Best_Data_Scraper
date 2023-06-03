import streamlit as st
import openai 
import pandas as pd
from bs4 import BeautifulSoup
from requests import get
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('THE BEST DATA SCRAPER')

st.markdown("""
This app performs simple webscraping of data from any webpage using ChatGPT prompt and BeautifulSoup
* **Python libraries:** base64, pandas, streamlit, requests, bs4, 
""")


openai.api_key = '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'

def get_completion(prompt, model="gpt-3.5-turbo", temperature=0): 
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
    )
    return response.choices[0].message["content"]

Features = st.text_input("Please enter the features")
st.write(Features)
print(Features=='Title')
# Type_of_Items = input("Enter the type of items you want to dowmnload their features :")
# Link = input("Enter the link of the page: ")
# Number_of_pages = input("Enter the number pages: ")


# prompt = f"""
# Your task is to provide the code that scrapes the {Features} of the {Type_of_Items} in {Number_of_pages} pages of the following web site whose link is : {Link} \
# Put the data into a dataframe whose variables will be {Features} \
# Use try and except python solution to exclude the errors when scraping the data \
# I just want the code nothing else and don't print the dataframe in the code 
# """
# response = get_completion(prompt)
# exec(response)

# st.dataframe(df)

# def filedownload(df):
#     csv = df.to_csv(index=False)
#     b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
#     href = f'<a href="data:file/csv;base64,{b64}" download="Vehicles_data.csv">Download CSV File</a>'
#     return href

# st.markdown(filedownload(df), unsafe_allow_html=True)

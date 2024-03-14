import requests
from api_key import api
import streamlit as st

st.set_page_config(layout="wide")

# Api url
url = f"https://api.nasa.gov/planetary/apod?api_key={api}"

# Get the request data
response1 = requests.get(url)
content = response1.json()
#print(content)

# Extract the image title, url and explanation
title = content["title"]
image_url = content["url"]
explanation = content["explanation"]

# Download the image
image_filepath = "img.png"
response2 = requests.get(image_url)

with open(image_filepath, "wb") as file:
    file.write(response2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)

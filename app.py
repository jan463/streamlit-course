import streamlit as st
import pandas as pd

######################### PAGE SETUP####################

# Set up the page
st.set_page_config(
    page_title="EV Adoption Tracker",
    layout="centered", # or wide
    page_icon="🚗", # choose your favorite icon
    initial_sidebar_state="collapsed" # or expanded
)

st.title("Creating your Superhero name")

color = st.text_input("Whats your favorite color? ", placeholder="very light Black")
animal = st.text_input("Whats your favorite animal? ", placeholder="Short necked Giraffe")
number = st.number_input("Whats your favorite number? ", step=1)
superpower = st.selectbox("Choose your Superpower:", ["flying", "invisibility", "super strength"])



if st.button("Generate my Superhero Name"):
    heroname = f"{color} {animal} of {number}"
    #st.markdown(f"You are *{heroname}* and your superpower is *{superpower}*")
    st.title(f" 🐔 You are {heroname}")

    st.subheader("Your Superhero Motto:")
    st.write(f"With great power comes great {superpower.lower()}!")
""" DODODOC: This is a sample code for using MSAL with Streamlit
    to authenticate users and access protected content. 
    It uses the streamlit_msal library for authentication.
    Make sure to set the CLIENT_ID and AUTHORITY environment variables in your .env file.
"""

from os import environ
import streamlit as st
from streamlit_msal import Msal

from dotenv import load_dotenv

load_dotenv()

# Use environment variables for sensitive information
CLIENT_ID = environ.get("CLIENT_ID")
AUTHORITY = environ.get("AUTHORITY")

with st.sidebar:
    auth_data = Msal.initialize_ui(
        client_id=CLIENT_ID,
        authority=AUTHORITY,
        scopes=[], # Optional
        # Customize (Default values):
        connecting_label="Connecting",
        disconnected_label="Disconnected",
        sign_in_label="Sign in",
        sign_out_label="Sign out"
    )

if not auth_data:
    st.write("Authenticate to access protected content")
    st.stop()

st.write("Protected content available")
access_token = auth_data["accessToken"]

account = auth_data["account"]
name = account["name"]
username = account["username"]
account_id = account["localAccountId"]


# Display information
st.write(f"Hello {name}!")
st.write(f"Your username is: {username}")
st.write(f"Your account id is: {account_id}")
st.write("Your access token is:")
st.code(access_token)

st.write("Auth data:")
st.json(auth_data)
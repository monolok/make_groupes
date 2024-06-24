from functions import create_groups
import streamlit as st
import pandas as pd
#from dotenv import load_dotenv
import os
#load_dotenv()
pass_answer=os.environ["PASS"]
# Initialize or get the current state of 'button_clicked'
if 'button_clicked' not in st.session_state:
    st.session_state['button_clicked'] = False

# Simple password input
password = st.text_input("Enter the password", type="password")

group_size = st.number_input("group_size", value=4)
# Check if the correct password is entered
if password == pass_answer:
    # Button to trigger the create_groups function
    if st.button('Create Groups'):
        st.session_state['button_clicked'] = True  # Update the state to indicate the button has been clicked
        groups = create_groups(group_size)
        st.write('Groups created:')
        df = pd.read_csv('data/file.csv')
        st.dataframe(df)
    else:
        st.write('Please enter the correct password')

# Display the dataframe only if the button has not been clicked
if not st.session_state['button_clicked']:
    df = pd.read_csv('data/file.csv')
    st.dataframe(df)
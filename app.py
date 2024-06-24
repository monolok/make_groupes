from functions import create_groups
import streamlit as st
import pandas as pd

# Initialize or get the current state of 'button_clicked'
if 'button_clicked' not in st.session_state:
    st.session_state['button_clicked'] = False

group_size = 3

# Button to trigger the create_groups function
if st.button('Create Groups'):
    st.session_state['button_clicked'] = True  # Update the state to indicate the button has been clicked
    groups = create_groups(group_size)
    st.write('Groups created:')
    df = pd.read_csv('data/file.csv')
    st.dataframe(df)

# Display the dataframe only if the button has not been clicked
if not st.session_state['button_clicked']:
    df = pd.read_csv('data/file.csv')
    st.dataframe(df)
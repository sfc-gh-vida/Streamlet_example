import streamlit as st
import pandas as pd
from snowflake_utils import fetch_snowflake_version, fetch_user_data, insert_user_data, fetch_last_user_id
from datetime import datetime

# Title and Text
st.title("My first Streamlit app")
st.header("This is a app Header")
st.write("This app is for practicing Streamlit components.")

# Fetch the last user ID and increment by 1
last_id = fetch_last_user_id()
new_user_id = last_id + 1

# Input Form
st.header("Add a New User")
with st.form(key='user_form'):
    user_id = st.number_input("User ID", min_value=1, value=new_user_id, step=1)
    user_name = st.text_input("User Name")
    created_on = st.date_input("Created On", datetime.now().date())
    
    # Convert the date input to a timestamp
    created_on_timestamp = datetime.combine(created_on, datetime.now().time())

    submit_button = st.form_submit_button(label='Add User')

# If the form is submitted, insert the data into Snowflake
if submit_button:
    insert_user_data(user_id, user_name, created_on_timestamp)
    st.success(f"User {user_name} added to the database!")


# Fetch and display user data from Snowflake
st.header("User Data from Snowflake")
user_data = fetch_user_data()

# Convert the user data into a DataFrame for better display
user_df = pd.DataFrame(user_data, columns=["ID", "Name", "Created On"])
# st.dataframe(user_df)
# st.write(user_df.style.hide_index())
st.table(user_df.set_index('ID'))

# Slider
age = st.slider("Select your age", 0, 100)
st.write(f"You are {age} years old")

# Button
if st.button("Click Me"):
    st.write("Button Clicked!")

# Displaying Data
data = pd.DataFrame({
    'Days': ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    'Study hours': [4, 6, 5, 7, 4]
})
st.table(data)

# Sidebar
st.sidebar.header("Sidebar Section")
st.sidebar.button("Sidebar Button")

# Snowflake Integration
st.header("Snowflake Data Integration")

# Fetch and display Snowflake version
version = fetch_snowflake_version()
st.write(f"Connected to Snowflake version: {version}")



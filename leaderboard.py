import streamlit as st
import pandas as pd
from Scoring import Cal_Score

# Define the page title
st.title("LeaderBoard")

# Function to load the leaderboard data from a file


def load_leaderboard(filename):
    try:
        leaderboard = pd.read_csv(filename)
    except FileNotFoundError:
        leaderboard = pd.DataFrame(columns=["User", "Precision_score"])
    return leaderboard

# Function to save the leaderboard data to a file


def save_leaderboard(leaderboard, filename):
    leaderboard.to_csv(filename, index=False)


# Define the filename for the leaderboard file
leaderboard_filename = "leaderboard.csv"

# Load the leaderboard from the file
leaderboard = load_leaderboard(leaderboard_filename)
# Display the leaderboard table

col1, col2 = st.columns(2)

# Allow users to enter their username
username = col1.text_input('Enter your username')
if username == '':
    st.info("Please enter your username")

# Allow users to upload their submission
file = col2.file_uploader('Upload your submission', type=['.joblib', '.pt'])
if file is not None:
    precision_score = Cal_Score(file)
    st.success("File uploaded successfully and computed.")
    if st.button("Add to LeaderBoard"):
        leaderboard.loc[len(leaderboard)] = [username, precision_score]
        save_leaderboard(leaderboard, leaderboard_filename)
        st.success("User added to the LeaderBoard.")

else:
    st.info("Please upload a file.")

# Display the leaderboard table
st.table(leaderboard)


# Add the user and precision score to the leaderboard

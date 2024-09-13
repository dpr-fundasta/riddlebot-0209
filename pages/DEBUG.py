import streamlit as st


import os
import sys

# Add parent directory to sys.path
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

# Import the variable from parent_file
from HOME import reasoning

score_style = """
    <style>
     .score-debug {
        font-size: 15px;
        font-weight: bold;
        color: #2c3e50;
    }
    </style>
"""

st.markdown("<div class='score-debug'>DEBUG TERMINAL：</div>", unsafe_allow_html=True)

# Display the 'reasoning' variable if it exists, otherwise handle the error gracefully


# Display the other session state variables
st.write("Database")
st.write(st.session_state.riddle_data)
st.write("History")
st.write(st.session_state.hint_history)
st.write("Reasoning")
try:
    # Code that may raise an exception
    st.write(reasoning)
except NameError:
    # Code that runs if the exception occurs
    st.write("Value not set")
# try:

#     st.write(reasoning)
# except AttributeError:
#     st.write("reasoning not set")


# import streamlit as st

# score_style = """
#     <style>
#      .score-debug {
#         font-size: 15px;
#         font-weight: bold;
#         color: #2c3e50;
#     }
#     </style>
# """

# st.markdown("<div class='score-debug'>DEBUG TERMINAL：</div>", unsafe_allow_html=True)
# st.write("Database")
# st.write(st.session_state.riddle_data)
# st.write("History")
# st.write(st.session_state.hint_history)

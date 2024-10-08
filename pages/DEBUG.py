import streamlit as st

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
    st.markdown(f'<p style="color:red;">{st.session_state.reasoning}</p>', unsafe_allow_html=True)
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

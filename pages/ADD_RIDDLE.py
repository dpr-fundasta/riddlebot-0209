import streamlit as st
st.set_page_config(page_title="📝 新しい謎を追加", page_icon="🌟")
from database.riddleFetch import  add_riddle
# Sidebar: Add a new riddle
st.title("📝 新しい謎を追加")
with st.form(key='riddle_form', clear_on_submit=True, border= True):
    question_input = st.text_input("謎の質問", st.session_state.get("question_input", ""))
    answer_input = st.text_input("正解の答え", st.session_state.get("answer_input", ""))
    reasoning_input = st.text_area("答えの理由（任意）", st.session_state.get("reasoning_input", ""))
    submit_button = st.form_submit_button(label="謎を追加")

if submit_button:
    if question_input and answer_input:
        reasoning_input = reasoning_input or ""
        add_riddle(question_input, answer_input, reasoning_input)
        st.toast("✅ 謎が正常に追加されました！")
        #st.sidebar.success("Riddle added successfully!")
        
        # Clear the sidebar text inputs
        st.session_state["question_input"] = ""
        st.session_state["answer_input"] = ""
        st.session_state["reasoning_input"] = ""
    else:
        #st.sidebar.error("Please fill out the required fields!")
        st.toast(" ⚠️ 必須項目をすべて入力してください！")
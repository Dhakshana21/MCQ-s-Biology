import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(
    page_title="Biology MCQ Practice",
    page_icon="🧬",
    layout="wide"
)

# Load Questions
@st.cache_data
def load_data():
    return pd.read_csv("biology_mcqs_shuffled.csv")

df = load_data()

# Session State
if "question_no" not in st.session_state:
    st.session_state.question_no = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "selected" not in st.session_state:
    st.session_state.selected = None

# Current Question
q = df.iloc[st.session_state.question_no]

st.title("🧬 Biology MCQ Practice Session")

st.markdown(
    f"### Question {st.session_state.question_no + 1} of {len(df)}"
)

st.write(q["Question"])

options = {
    "A": q["Option_A"],
    "B": q["Option_B"],
    "C": q["Option_C"],
    "D": q["Option_D"]
}

selected = st.radio(
    "Choose your answer:",
    list(options.keys()),
    format_func=lambda x: f"{x}. {options[x]}",
    key=f"q_{st.session_state.question_no}"
)

# Submit
if st.button("Submit Answer"):

    st.session_state.answered = True

    if selected == q["Answer"]:
        st.success("✅ Correct Answer")
        st.session_state.score += 1
    else:
        st.error("❌ Wrong Answer")

        correct_option = q["Answer"]
        st.info(
            f"Correct Answer: {correct_option}. "
            f"{options[correct_option]}"
        )

# Next Question
if st.session_state.answered:

    if st.button("Next Question"):

        st.session_state.question_no += 1
        st.session_state.answered = False

        if st.session_state.question_no >= len(df):

            st.balloons()

            st.success(
                f"Quiz Completed!\n\n"
                f"Score: {st.session_state.score}/{len(df)}"
            )

            st.stop()

        st.rerun()

# Sidebar
st.sidebar.title("Progress")

st.sidebar.metric(
    "Current Score",
    st.session_state.score
)

st.sidebar.metric(
    "Question",
    f"{st.session_state.question_no + 1}/{len(df)}"
)
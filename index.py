import streamlit as st
import random

st.set_page_config(page_title="Guess the Number Game")

st.title("🎯 Guess the Number Game")

# Initialize session state variables
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.guess_history = []

st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

# User input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    st.session_state.attempts += 1
    st.session_state.guess_history.append(guess)

    if guess < st.session_state.number:
        st.warning("Too low! Try again.")
    elif guess > st.session_state.number:
        st.warning("Too high! Try again.")
    else:
        st.success(f"🎉 Correct! The number was {st.session_state.number}.")
        st.balloons()
        st.info(f"You guessed it in {st.session_state.attempts} attempts.")
        if st.button("Play Again"):
            st.session_state.number = random.randint(1, 100)
            st.session_state.attempts = 0
            st.session_state.guess_history = []

# Optional: show history of guesses
with st.expander("Show Guess History"):
    st.write(st.session_state.guess_history)

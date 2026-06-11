import random
import streamlit as st
from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
    is_valid_range,
    is_high_score,
)

st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.markdown("""
<style>
div[data-testid="stTextInput"] input,
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background-color: #E7F1FE;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.header("Settings")

if "difficulty" not in st.session_state:
    st.session_state.difficulty = "Normal"

difficulty = st.session_state.difficulty

st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=["Easy", "Normal", "Hard"].index(difficulty),
    key="sidebar_difficulty",
    disabled=True,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    st.session_state.attempts = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []

if "show_hint" not in st.session_state:
    st.session_state.show_hint = True

if "debug_open" not in st.session_state:
    st.session_state.debug_open = False

if "game_count" not in st.session_state:
    st.session_state.game_count = 0

if "high_score" not in st.session_state:
    st.session_state.high_score = 0

st.sidebar.metric("High Score", st.session_state.high_score)

st.subheader("Make a guess")

st.info("Guess a number between 1 and 100.")

with st.form(key="guess_form", clear_on_submit=True):
    raw_guess = st.text_input(
        "Enter your guess:",
        key=f"guess_input_{difficulty}_{st.session_state.game_count}"
    )
    submit = st.form_submit_button("Submit Guess 🚀")

col_hint, col_diff, col_ng = st.columns([1, 1, 1])
with col_hint:
    st.session_state.show_hint = st.checkbox(
        "Show hint", value=st.session_state.show_hint
    )
with col_diff:
    selected_difficulty = st.selectbox(
        "Difficulty",
        ["Easy", "Normal", "Hard"],
        index=["Easy", "Normal", "Hard"].index(st.session_state.difficulty),
        label_visibility="collapsed",
    )
    if selected_difficulty != st.session_state.difficulty:
        st.session_state.difficulty = selected_difficulty
        st.session_state.attempts = 0
        new_low, new_high = get_range_for_difficulty(selected_difficulty)
        st.session_state.secret = random.randint(new_low, new_high)
        st.session_state.status = "playing"
        st.session_state.history = []
        st.session_state.score = 0
        st.session_state.game_count += 1
        st.rerun()
with col_ng:
    new_game = st.button("New Game 🔁", use_container_width=True)

show_hint = st.session_state.show_hint

if submit:
    st.session_state.attempts += 1

st.info(f"Attempts left: {attempt_limit - st.session_state.attempts}")

if new_game:
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(1, 100)
    st.session_state.status = "playing"
    st.session_state.history = []
    st.session_state.score = 0
    st.session_state.game_count += 1
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.session_state.attempts -= 1
        st.error(err)
    elif not is_valid_range(guess_int, low, high):
        st.session_state.attempts -= 1
        st.error(f"Guess must be between {low} and {high}.")
    elif guess_int in st.session_state.history:
        st.session_state.attempts -= 1
        st.error(
            f"{guess_int} has already been guessed. Try a different number."
        )
    else:
        st.session_state.history.append(guess_int)

        outcome, message = check_guess(guess_int, st.session_state.secret)

        st.session_state.score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )

        if outcome == "Win":
            points = max(10, 100 - 10 * (st.session_state.attempts - 1))
            if show_hint:
                st.warning(
                    f"{message}  |  Score: +{points} points for winning"
                    f" in {st.session_state.attempts} attempt(s)."
                )
        else:
            if show_hint:
                st.warning(f"{message}  |  Score: −5 points.")

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            if is_high_score(
                st.session_state.score, st.session_state.high_score
            ):
                st.session_state.high_score = st.session_state.score
                st.success("🏆 New High Score!")
            incorrect = st.session_state.attempts - 1
            deduction = incorrect * 5
            guess_label = "guess" if incorrect == 1 else "guesses"
            st.success(
                f"You won! The secret was {st.session_state.secret}. "
                f"Final score: {st.session_state.score} "
                f"(−{deduction} points for {incorrect} incorrect"
                f" {guess_label}.)"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                final_score = max(10, st.session_state.score)
                st.session_state.score = final_score
                incorrect = st.session_state.attempts
                deduction = incorrect * 5
                guess_label = "guess" if incorrect == 1 else "guesses"
                st.error(
                    f"Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Final score: {final_score} "
                    f"(−{deduction} points for {incorrect}"
                    f" incorrect {guess_label}.)"
                )

st.session_state.debug_open = st.checkbox(
    "Show Developer Debug Info", value=st.session_state.debug_open
)

with st.expander("Developer Debug Info", expanded=st.session_state.debug_open):
    st.write("Secret:", st.session_state.secret)
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")

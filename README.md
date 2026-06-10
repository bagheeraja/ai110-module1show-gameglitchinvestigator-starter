# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
   - This game is a simple number guessing game. Players can choose from three different difficulty levels. Each level adjusts both the number of guesses and the range of numbers in the selection pool. Historical guesses are tracked to prevent duplicate guesses. Attempts remaining are tracked. Hints are provided based on the comparison of the guess and the secret number. Incorrect guesses come with a penalty of -5 points. Wins are weighted by the number of guesses needed to achieve the win.
- [ ] Detail which bugs you found.
   - A number of bugs were found. Bug fixes are presented in a table below in the Summary of Changes section.
- [ ] Explain what fixes you applied.
   - Fixes are also presented in the table below in the Summary of Changes section.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Launch the app with `python -m streamlit run app.py`. The game opens with **Normal** difficulty selected (range 1–100, 8 attempts). Use the difficulty dropdown next to the buttons to switch to **Easy** (1–20, 6 attempts) or **Hard** (1–50, 5 attempts) at any time — changing difficulty automatically resets the game.
2. The blue info bar at the top shows the instructions and the current number of **Attempts Left**. Type a whole number into the **Enter your guess** field and press **Enter** or click **Submit Guess**. Entering a letter, decimal, duplicate, or out-of-range number displays an error and does not consume an attempt.
3. After each guess a hint appears — **📉 Go HIGHER!** or **📈 Go LOWER!** — followed by the score change for that turn (e.g. *Score: −5 points*). The Attempts Left counter decrements by one with each valid guess.
4. Keep narrowing your guess using the hints. When you guess correctly, **🎉 Correct!** appears alongside your win bonus. The final success message shows your score, the total deduction for incorrect guesses, and how many attempts you used (e.g. *You won! The secret was 42. Final score: 65 (−15 points for 3 incorrect guesses.)*).
5. If you run out of attempts the game ends with a loss message showing the secret number and your final score (minimum 10). Click **New Game** at any time to reset all state — score, history, attempts, and the guess field — and start a fresh round.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
============================= test session starts ==============================
platform darwin -- Python 3.12.0, pytest-9.0.3, pluggy-1.6.0 -- /Users/bagheera/repos/codepath/Codepath_AI_110/Week02/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/bagheera/repos/codepath/Codepath_AI_110/Week02
plugins: anyio-4.13.0
collecting ... collected 47 items

tests/test_game_logic.py::TestGetRangeForDifficulty::test_easy_range PASSED [  2%]
tests/test_game_logic.py::TestGetRangeForDifficulty::test_normal_range PASSED [  4%]
tests/test_game_logic.py::TestGetRangeForDifficulty::test_hard_range PASSED [  6%]
tests/test_game_logic.py::TestGetRangeForDifficulty::test_unknown_difficulty_returns_default PASSED [  8%]
tests/test_game_logic.py::TestGetRangeForDifficulty::test_empty_string_returns_default PASSED [ 10%]
tests/test_game_logic.py::TestParseGuess::test_valid_integer PASSED      [ 12%]
tests/test_game_logic.py::TestParseGuess::test_valid_integer_boundary_low PASSED [ 14%]
tests/test_game_logic.py::TestParseGuess::test_valid_integer_boundary_high PASSED [ 17%]
tests/test_game_logic.py::TestParseGuess::test_none_input PASSED         [ 19%]
tests/test_game_logic.py::TestParseGuess::test_empty_string PASSED       [ 21%]
tests/test_game_logic.py::TestParseGuess::test_letter_input PASSED       [ 23%]
tests/test_game_logic.py::TestParseGuess::test_word_input PASSED         [ 25%]
tests/test_game_logic.py::TestParseGuess::test_decimal_input PASSED      [ 27%]
tests/test_game_logic.py::TestParseGuess::test_decimal_with_zero_fraction PASSED [ 29%]
tests/test_game_logic.py::TestParseGuess::test_negative_integer PASSED   [ 31%]
tests/test_game_logic.py::TestParseGuess::test_zero PASSED               [ 34%]
tests/test_game_logic.py::TestCheckGuess::test_correct_guess_returns_win PASSED [ 36%]
tests/test_game_logic.py::TestCheckGuess::test_correct_guess_message PASSED [ 38%]
tests/test_game_logic.py::TestCheckGuess::test_guess_too_high_outcome PASSED [ 40%]
tests/test_game_logic.py::TestCheckGuess::test_guess_too_high_message_says_lower PASSED [ 42%]
tests/test_game_logic.py::TestCheckGuess::test_guess_too_low_outcome PASSED [ 44%]
tests/test_game_logic.py::TestCheckGuess::test_guess_too_low_message_says_higher PASSED [ 46%]
tests/test_game_logic.py::TestCheckGuess::test_boundary_one_below_secret PASSED [ 48%]
tests/test_game_logic.py::TestCheckGuess::test_boundary_one_above_secret PASSED [ 51%]
tests/test_game_logic.py::TestCheckGuess::test_returns_tuple_of_two PASSED [ 53%]
tests/test_game_logic.py::TestUpdateScore::test_win_on_first_attempt_scores_100 PASSED [ 55%]
tests/test_game_logic.py::TestUpdateScore::test_win_on_second_attempt_scores_90 PASSED [ 57%]
tests/test_game_logic.py::TestUpdateScore::test_win_on_tenth_attempt_hits_floor PASSED [ 59%]
tests/test_game_logic.py::TestUpdateScore::test_win_beyond_tenth_attempt_still_floors_at_10 PASSED [ 61%]
tests/test_game_logic.py::TestUpdateScore::test_win_adds_to_existing_score PASSED [ 63%]
tests/test_game_logic.py::TestUpdateScore::test_too_high_deducts_5 PASSED [ 65%]
tests/test_game_logic.py::TestUpdateScore::test_too_low_deducts_5 PASSED [ 68%]
tests/test_game_logic.py::TestUpdateScore::test_too_high_and_too_low_deduct_equally PASSED [ 70%]
tests/test_game_logic.py::TestUpdateScore::test_score_can_go_negative PASSED [ 72%]
tests/test_game_logic.py::TestUpdateScore::test_unknown_outcome_leaves_score_unchanged PASSED [ 74%]
tests/test_game_logic.py::TestUpdateScore::test_cumulative_deductions PASSED [ 76%]
tests/test_game_logic.py::TestIsValidRange::test_easy_low_boundary_valid PASSED [ 78%]
tests/test_game_logic.py::TestIsValidRange::test_easy_high_boundary_valid PASSED [ 80%]
tests/test_game_logic.py::TestIsValidRange::test_easy_mid_range_valid PASSED [ 82%]
tests/test_game_logic.py::TestIsValidRange::test_easy_zero_is_invalid PASSED [ 85%]
tests/test_game_logic.py::TestIsValidRange::test_easy_negative_is_invalid PASSED [ 87%]
tests/test_game_logic.py::TestIsValidRange::test_easy_above_high_is_invalid PASSED [ 89%]
tests/test_game_logic.py::TestIsValidRange::test_hard_high_boundary_valid PASSED [ 91%]
tests/test_game_logic.py::TestIsValidRange::test_hard_above_high_is_invalid PASSED [ 93%]
tests/test_game_logic.py::TestIsValidRange::test_normal_high_boundary_valid PASSED [ 95%]
tests/test_game_logic.py::TestIsValidRange::test_normal_above_high_is_invalid PASSED [ 97%]
tests/test_game_logic.py::TestIsValidRange::test_normal_zero_is_invalid PASSED [100%]

============================== 47 passed in 0.04s ==============================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]

## Summary of Changes

### Bug Fixes

| Bug | Root Cause | Fix |
|---|---|---|
| Attempts Left showed 7 instead of 8 | `st.session_state.attempts` initialized to `1` | Changed initialization to `0` |
| Attempts Left always one behind | `st.info` rendered before the increment in Streamlit's top-down rerun | Moved display to after the increment |
| New Game button had no effect after game over | Handler never reset `st.session_state.status` back to `"playing"` | Added `status = "playing"` to the reset block |
| Hints were wrong on even-numbered turns | Submit block cast `secret` to a string on even attempts, causing lexicographic comparisons | Removed type coercion; `check_guess` always receives two integers |
| "Go HIGHER" / "Go LOWER" directions reversed in edge case | `check_guess` except branch had the messages swapped | Corrected the message strings |
| Invalid guesses (letters, out-of-range) added to history | `history.append` called before validation checks | Removed append from all invalid-input branches |
| Developer Debug window closed on every Submit | `st.expander` has no built-in state persistence across reruns | Persisted open/closed state in `st.session_state.debug_open` via a checkbox |
| Show Hint reset after every guess | Checkbox was inside `st.form`, which clears on submit | Moved outside the form; backed by `st.session_state.show_hint` |
| Previous guess remained in input after New Game | Streamlit reuses widget state when the key is unchanged | Added `game_count` to session state and included it in the input key |

### Features Added

- **Duplicate guess detection** — guesses already in history are rejected without consuming an attempt
- **Decimal rejection** — decimal inputs return an error instead of being silently rounded down
- **Range validation** — out-of-range guesses rejected without consuming an attempt; logic extracted to `is_valid_range()` in `logic_utils.py`
- **Enter key submits** — input and Submit button wrapped in `st.form` so pressing Enter works as expected
- **In-game difficulty selector** — dropdown added alongside the buttons; changing difficulty starts a fresh game automatically
- **Symmetric scoring** — replaced inconsistent even/odd attempt bonus logic with a flat −5 penalty per wrong guess and a win bonus of `max(10, 100 − 10 × (attempts − 1))`
- **Per-guess score feedback** — score change appended to the hint message each turn (e.g. *📉 Go HIGHER! | Score: −5 points.*)
- **Detailed win/loss messages** — both now show final score, total deduction, and incorrect guess count

### Refactoring

- **`logic_utils.py`** — populated with all five pure game functions: `get_range_for_difficulty`, `parse_guess`, `check_guess`, `update_score`, and `is_valid_range`
- **`app.py`** — removed duplicate function definitions; now imports all logic from `logic_utils`

### Test Suite

47 tests across 5 classes in `tests/test_game_logic.py`:

| Class | What it covers |
|---|---|
| `TestGetRangeForDifficulty` | All three difficulty levels and the unknown/default fallback |
| `TestParseGuess` | Valid integers, empty/None input, letters, decimals, negatives, and boundary values |
| `TestCheckGuess` | Win, Too High, Too Low, one-off boundaries, and return type |
| `TestUpdateScore` | Win bonus at various attempt counts including the floor, symmetric penalties, negative scores, cumulative deductions, and unknown outcomes |
| `TestIsValidRange` | Low and high boundaries, mid-range, zero, negative, and one-above-high for all three difficulty ranges |

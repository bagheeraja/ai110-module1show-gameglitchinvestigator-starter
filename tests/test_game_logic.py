from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score, is_valid_range, is_high_score


# ---------------------------------------------------------------------------
# get_range_for_difficulty
# ---------------------------------------------------------------------------

class TestGetRangeForDifficulty:
    def test_easy_range(self):
        assert get_range_for_difficulty("Easy") == (1, 20)

    def test_normal_range(self):
        assert get_range_for_difficulty("Normal") == (1, 100)

    def test_hard_range(self):
        assert get_range_for_difficulty("Hard") == (1, 50)

    def test_unknown_difficulty_returns_default(self):
        assert get_range_for_difficulty("Impossible") == (1, 100)

    def test_empty_string_returns_default(self):
        assert get_range_for_difficulty("") == (1, 100)


# ---------------------------------------------------------------------------
# parse_guess
# ---------------------------------------------------------------------------

class TestParseGuess:
    def test_valid_integer(self):
        ok, value, err = parse_guess("42")
        assert ok is True
        assert value == 42
        assert err is None

    def test_valid_integer_boundary_low(self):
        ok, value, _ = parse_guess("1")
        assert ok is True
        assert value == 1

    def test_valid_integer_boundary_high(self):
        ok, value, _ = parse_guess("100")
        assert ok is True
        assert value == 100

    def test_none_input(self):
        ok, value, err = parse_guess(None)
        assert ok is False
        assert value is None
        assert err == "Enter a guess."

    def test_empty_string(self):
        ok, value, err = parse_guess("")
        assert ok is False
        assert value is None
        assert err == "Enter a guess."

    def test_letter_input(self):
        ok, value, err = parse_guess("p")
        assert ok is False
        assert value is None
        assert err == "That is not a number."

    def test_word_input(self):
        ok, value, err = parse_guess("hello")
        assert ok is False
        assert value is None
        assert err == "That is not a number."

    def test_decimal_input(self):
        ok, value, err = parse_guess("3.5")
        assert ok is False
        assert value is None
        assert err == "Enter a whole number, not a decimal."

    def test_decimal_with_zero_fraction(self):
        ok, _, err = parse_guess("50.0")
        assert ok is False
        assert err == "Enter a whole number, not a decimal."

    def test_negative_integer(self):
        ok, value, _ = parse_guess("-5")
        assert ok is True
        assert value == -5

    def test_zero(self):
        ok, value, _ = parse_guess("0")
        assert ok is True
        assert value == 0

    def test_whitespace_only(self):
        ok, value, err = parse_guess("   ")
        assert ok is False
        assert value is None
        assert err == "Enter a guess."

    def test_leading_trailing_spaces_parse_successfully(self):
        ok, value, _ = parse_guess(" 42 ")
        assert ok is True
        assert value == 42

    def test_very_large_integer(self):
        ok, value, _ = parse_guess("999999999")
        assert ok is True
        assert value == 999999999

    def test_negative_decimal(self):
        ok, _, err = parse_guess("-3.5")
        assert ok is False
        assert err == "Enter a whole number, not a decimal."

    def test_multiple_decimal_points(self):
        ok, _, err = parse_guess("1.2.3")
        assert ok is False
        assert err == "Enter a whole number, not a decimal."

    def test_scientific_notation(self):
        ok, _, err = parse_guess("1e2")
        assert ok is False
        assert err == "That is not a number."


# ---------------------------------------------------------------------------
# check_guess
# ---------------------------------------------------------------------------

class TestCheckGuess:
    def test_correct_guess_returns_win(self):
        outcome, _ = check_guess(50, 50)
        assert outcome == "Win"

    def test_correct_guess_message(self):
        _, message = check_guess(50, 50)
        assert "Correct" in message

    def test_guess_too_high_outcome(self):
        outcome, _ = check_guess(60, 50)
        assert outcome == "Too High"

    def test_guess_too_high_message_says_lower(self):
        _, message = check_guess(60, 50)
        assert "LOWER" in message

    def test_guess_too_low_outcome(self):
        outcome, _ = check_guess(40, 50)
        assert outcome == "Too Low"

    def test_guess_too_low_message_says_higher(self):
        _, message = check_guess(40, 50)
        assert "HIGHER" in message

    def test_boundary_one_below_secret(self):
        outcome, _ = check_guess(49, 50)
        assert outcome == "Too Low"

    def test_boundary_one_above_secret(self):
        outcome, _ = check_guess(51, 50)
        assert outcome == "Too High"

    def test_returns_tuple_of_two(self):
        result = check_guess(50, 50)
        assert isinstance(result, tuple)
        assert len(result) == 2

    def test_both_zero_is_win(self):
        outcome, _ = check_guess(0, 0)
        assert outcome == "Win"

    def test_very_large_values_too_low(self):
        outcome, _ = check_guess(999999, 1000000)
        assert outcome == "Too Low"

    def test_negative_secret_win(self):
        outcome, _ = check_guess(-5, -5)
        assert outcome == "Win"

    def test_negative_secret_too_high(self):
        outcome, _ = check_guess(-1, -5)
        assert outcome == "Too High"

    def test_negative_secret_too_low(self):
        outcome, _ = check_guess(-10, -5)
        assert outcome == "Too Low"


# ---------------------------------------------------------------------------
# update_score
# ---------------------------------------------------------------------------

class TestUpdateScore:
    def test_win_on_first_attempt_scores_100(self):
        assert update_score(0, "Win", 1) == 100

    def test_win_on_second_attempt_scores_90(self):
        assert update_score(0, "Win", 2) == 90

    def test_win_on_tenth_attempt_hits_floor(self):
        assert update_score(0, "Win", 10) == 10

    def test_win_beyond_tenth_attempt_still_floors_at_10(self):
        assert update_score(0, "Win", 15) == 10

    def test_win_adds_to_existing_score(self):
        assert update_score(50, "Win", 1) == 150

    def test_too_high_deducts_5(self):
        assert update_score(100, "Too High", 3) == 95

    def test_too_low_deducts_5(self):
        assert update_score(100, "Too Low", 3) == 95

    def test_too_high_and_too_low_deduct_equally(self):
        high_result = update_score(100, "Too High", 3)
        low_result = update_score(100, "Too Low", 3)
        assert high_result == low_result

    def test_score_can_go_negative(self):
        assert update_score(0, "Too Low", 1) == -5

    def test_unknown_outcome_leaves_score_unchanged(self):
        assert update_score(75, "Draw", 1) == 75

    def test_cumulative_deductions(self):
        score = 0
        score = update_score(score, "Too Low", 1)
        score = update_score(score, "Too High", 2)
        score = update_score(score, "Too Low", 3)
        assert score == -15

    def test_win_on_attempt_zero_clamped_to_attempt_one(self):
        assert update_score(0, "Win", 0) == 100

    def test_win_with_very_large_attempt_number(self):
        assert update_score(0, "Win", 1000) == 10

    def test_win_floor_applied_to_total(self):
        assert update_score(-35, "Win", 8) == 10

    def test_outcome_is_case_sensitive(self):
        assert update_score(100, "win", 1) == 100
        assert update_score(100, "WIN", 1) == 100
        assert update_score(100, "too high", 1) == 100


# ---------------------------------------------------------------------------
# is_valid_range
# ---------------------------------------------------------------------------

class TestIsValidRange:
    # Easy range: 1–20
    def test_easy_low_boundary_valid(self):
        assert is_valid_range(1, 1, 20) is True

    def test_easy_high_boundary_valid(self):
        assert is_valid_range(20, 1, 20) is True

    def test_easy_mid_range_valid(self):
        assert is_valid_range(10, 1, 20) is True

    def test_easy_zero_is_invalid(self):
        assert is_valid_range(0, 1, 20) is False

    def test_easy_negative_is_invalid(self):
        assert is_valid_range(-5, 1, 20) is False

    def test_easy_above_high_is_invalid(self):
        assert is_valid_range(21, 1, 20) is False

    # Hard range: 1–50
    def test_hard_high_boundary_valid(self):
        assert is_valid_range(50, 1, 50) is True

    def test_hard_above_high_is_invalid(self):
        assert is_valid_range(51, 1, 50) is False

    # Normal range: 1–100
    def test_normal_high_boundary_valid(self):
        assert is_valid_range(100, 1, 100) is True

    def test_normal_above_high_is_invalid(self):
        assert is_valid_range(101, 1, 100) is False

    def test_normal_zero_is_invalid(self):
        assert is_valid_range(0, 1, 100) is False

    def test_very_large_integer_invalid(self):
        assert is_valid_range(999999, 1, 100) is False

    def test_very_large_negative_invalid(self):
        assert is_valid_range(-999999, 1, 100) is False

    def test_single_value_range_valid(self):
        assert is_valid_range(5, 5, 5) is True

    def test_single_value_range_below_invalid(self):
        assert is_valid_range(4, 5, 5) is False

    def test_single_value_range_above_invalid(self):
        assert is_valid_range(6, 5, 5) is False


# ---------------------------------------------------------------------------
# is_high_score
# ---------------------------------------------------------------------------

class TestIsHighScore:
    def test_higher_score_is_new_high(self):
        assert is_high_score(90, 80) is True

    def test_equal_score_is_not_new_high(self):
        assert is_high_score(80, 80) is False

    def test_lower_score_is_not_new_high(self):
        assert is_high_score(70, 80) is False

    def test_first_game_any_positive_score_beats_zero(self):
        assert is_high_score(10, 0) is True

    def test_zero_does_not_beat_zero(self):
        assert is_high_score(0, 0) is False

    def test_score_beats_previous_high_by_one(self):
        assert is_high_score(81, 80) is True

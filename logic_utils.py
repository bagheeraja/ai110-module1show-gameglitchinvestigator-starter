def get_range_for_difficulty(difficulty: str):
    """Return the inclusive number range for a given difficulty level.

    Args:
        difficulty: The difficulty level. Accepted values are "Easy",
            "Normal", and "Hard". Any other value returns the Normal range.

    Returns:
        A tuple (low, high) representing the inclusive guessing range.
        Easy: (1, 20), Normal: (1, 100), Hard: (1, 50).
        Defaults to (1, 100) for unrecognised difficulty values.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """Parse raw text input from the player into a validated integer guess.

    Rejects None, empty strings, whitespace-only strings, decimals,
    and non-numeric input. Does not enforce range bounds — that is the
    responsibility of is_valid_range().

    Args:
        raw: The raw string value from the text input field. May be
            None, empty, or contain non-numeric characters.

    Returns:
        A tuple (ok, guess_int, error_message) where:
            ok (bool): True if the input was successfully parsed.
            guess_int (int | None): The parsed integer, or None if invalid.
            error_message (str | None): A player-facing error string if
                ok is False, otherwise None.
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            return False, None, "Enter a whole number, not a decimal."
        value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """Compare a player's guess to the secret number and return a result.

    Args:
        guess (int): The player's guessed value.
        secret (int): The secret number to guess.

    Returns:
        A tuple (outcome, message) where:
            outcome (str): One of "Win", "Too High", or "Too Low".
            message (str): A player-facing hint string with an emoji.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📈 Go LOWER!"
        else:
            return "Too Low", "📉 Go HIGHER!"
    except TypeError:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📈 Go HIGHER!"
        return "Too Low", "📉 Go LOWER!"


def is_high_score(current_score: int, high_score: int) -> bool:
    """Determine whether a score beats the current session high score.

    Args:
        current_score: The score achieved in the most recently completed game.
        high_score: The best score recorded so far in the session.

    Returns:
        True if current_score strictly exceeds high_score, False otherwise.
        Equal scores do not qualify as a new high score.
    """
    return current_score > high_score


def is_valid_range(guess: int, low: int, high: int) -> bool:
    """Check whether a guess falls within the allowed range for the current
    game.

    Both low and high are inclusive boundaries. Range values are provided
    by get_range_for_difficulty().

    Args:
        guess: The integer value the player entered.
        low: The minimum valid value (inclusive).
        high: The maximum valid value (inclusive).

    Returns:
        True if low <= guess <= high, False otherwise.
    """
    return low <= guess <= high


def update_score(current_score: int, outcome: str, attempt_number: int) -> int:
    """Calculate and return the updated score after a guess.

    On a win, awards a bonus of max(10, 100 - 10 * (attempt_number - 1)),
    then applies a floor so the total never falls below 10. On an incorrect
    guess, deducts 5 points from the running total with no floor applied.
    attempt_number is clamped to a minimum of 1 to prevent invalid bonuses.

    Args:
        current_score: The player's score before this guess.
        outcome: The result of the guess. One of "Win", "Too High",
            or "Too Low". Any other value leaves the score unchanged.
        attempt_number: The 1-based number of attempts used so far,
            including the current guess.

    Returns:
        The updated integer score. May be negative for wrong guesses.
        Guaranteed to be at least 10 on a winning guess.
    """
    if outcome == "Win":
        attempt_number = max(1, attempt_number)
        points = max(10, 100 - 10 * (attempt_number - 1))
        return max(10, current_score + points)
    if outcome in ("Too High", "Too Low"):
        return current_score - 5
    return current_score

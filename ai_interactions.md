# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->
> Provide a step by step explanation of the process to add a High Score Tracking feature to the existing code base. Also indicate whether this feature is best incorporated within a current file or best developed as an independent file and imported into the App.

After the Summary below was developed, the following prompt was used: Complete steps 1-7 a single step at a time for review and confirmation.

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->
##Summary
| --- | --- | --- |
| Step | File | Action
| 1 | logic_utils.py | Add is_high_score function
| 2 | app.py | Initialize high_score in session state
| 3 | app.py | Import is_high_score
| 4 | app.py | Check and update high score in win block
| 5 | app.py | Display high score in sidebar
| 6 | app.py | Confirm New Game does not reset high score
| 7 | test_game_logic.py | Add TestIsHighScore test class

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->
In this process, the code modifications for each step were reviewed, approved, and completed prior to any work on the next step. However, no manual corrections were necessary during the process.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Whitespace-only input (`" "`) | "Find additional edge cases that might undermine the logic in logic_utils.py. Edge cases can be negative numbers, decimals, extremely large values, etc." | `parse_guess(" ")` returns `(False, None, "Enter a guess.")` | No — initially returned "That is not a number." | The `raw == ""` check didn't catch strings that were non-empty but contained only spaces. Fixed by changing the check to `raw.strip() == ""`. |
| Win on attempt 0 (`update_score(0, "Win", 0)`) | Same prompt as above | `update_score(0, "Win", 0) == 100` | No — returned 110 | `attempt_number - 1` evaluated to `-1`, yielding `100 - 10 * -1 = 110`. Fixed by clamping with `max(1, attempt_number)` before the calculation. |
| Win floor applied to total (`update_score(-35, "Win", 8)`) | Same prompt as above | `update_score(-35, "Win", 8) == 10` | No — returned -5 | The `max(10, ...)` floor only guarded the win bonus points, not the running total. Fixed by applying `max(10, current_score + points)` to the full return value. |
| Scientific notation (`parse_guess("1e2")`) | Same prompt as above | `parse_guess("1e2")` returns `(False, None, "That is not a number.")` | Yes | `"1e2"` contains no `.` so it bypasses the decimal check, then `int("1e2")` raises `ValueError`. The existing exception handler correctly catches it. No code change needed — test documents confirmed behavior. |
| Very large integer (`parse_guess("999999999")`) | Same prompt as above | `parse_guess("999999999")` returns `(True, 999999999, None)` | Yes | The parser has no upper bound — by design, range enforcement is the job of `is_valid_range`, not the parser. Test documents the intentional separation of concerns. |
| Negative secret number (`check_guess(-1, -5)`) | Same prompt as above | `check_guess(-1, -5)` returns `("Too High", ...)` | Yes | This test is not meaningful for this game. All difficulty ranges start at 1, so a negative secret number cannot occur in normal play. The test was generated as a general edge case but does not reflect any real game scenario and could reasonably be removed as it tests an impossible condition. |
| Win floor for `is_valid_range` with extreme values (`is_valid_range(999999, 1, 100)`) | Same prompt as above | `is_valid_range(999999, 1, 100) == False` | Yes | The `low <= guess <= high` expression handles arbitrarily large values correctly without overflow. Test documents confirmed behavior. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->

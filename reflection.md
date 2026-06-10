# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. The hints are reversed. An input of 100 returns a hint of Go Higher. An input of 1 returns a hint of Go Lower. The range of the guessing game should be from 1-100.
  2. The game does not start with the correct number of Attempts Left. The counter should start at 8, but it starts at 7.
  3. A glitch related to #2 is that the Attempts Left does not decrease after the first turn is completed. It counter remains at 7.
  4. The Game Over message displays when the New Game button is pressed. The game does not restart unless the browser page is refreshed.
  5. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Guess of 1 | "Go Higher" hint | "Go Lower" hint| none |
|Guess of 100 | "Go Lower" hint | "Go Higher hint | none |
| "New Game" pressed | Game resets | Game does not reset | none |
| Guess entered | Guess added to tracking array | Only every other guess is added | none |
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). The st.session_state.attempts was initialized to 1 resulting in an incorrect count of remaining attempts in the game from the start.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

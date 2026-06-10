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
| Enter key pressed | Guess entered would be processed| Nothing happened | No error|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). The AI suggested that every other guess was being converted to a string which resulted in a bad comparison to the Secret and prevented the guess from being successfully appended to the History array.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). In this case, the AI indication that the top-to-bottom execution order was causing the Attempts Left counter to lag one step behind was misleading. The other aspect of the issue was that two items, the game instructions and the Attempts Left were set up in the same component. If left together, either the directions could not be at the top or the Attempts Left could not be calculated correctly during a turn. My solution was to divide them up so the directions could still live at the top of the game screen while the Attempts Left could be moved to the bottom so the calculation could be processed in the correct order according to Streamlit's execution order.

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

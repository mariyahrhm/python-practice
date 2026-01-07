## How to Play- General knowledge quiz:
1. Run the script in a Python environment.
2. Enter your name when prompted.
3. Choose a difficulty level:
   - `E` for Easy
   - `M` for Medium
   - `H` for Hard
4. Answer each question by typing `a`, `b`, or `c`.
5. At the end, your score will be displayed.
6. When asked "Play again?", type `y` to restart or `n` to exit.


## Technical Documentation:

The quiz logic is inside a function run_quiz().

Each difficulty level has its own set of questions which the user can choose. If input not recognised then the output states "Sorry, I didn't recognise that level. Please choose E, M, or H."

The quiz uses branching `if`/`elif`/`else` conditioned by user input to determine which set of instructions to execute which runs in one block.

The user is able to type their own answers via the input() function.

The variable score starts at 0 and counts (score += 1) correct answers, the score is displayed at the end.

A while True loop allows replay until the user enters `n` to stop the quiz.

## Limitations:

Exact letter matching for levels: requires `E`, `M`, or `H` in uppercase

Hard‑coded questions: Changing quiz content requires editing the code.


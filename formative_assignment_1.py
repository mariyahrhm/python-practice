

def run_quiz():

    name = input("What is your name?")
    print("Choose your level of difficulty")
    print("E: easy")
    print("M: medium")
    print("H: hard")
    level = input("which one would you like to choose?")

    score = 0

    if level == "E":
        print("you chose easy level, great! Let's get started.")

        print("Question 1: What colour is the sky?")
        print("a) blue")
        print("b) green")
        print("c) yellow")

        equestion1 = input("Your answer:")
        if equestion1 == "a" :
            print("Correct, let's go to the next question.")
            score += 1
        else:
            print("incorrect, next question...")


        print("Question 2: how many tentacles does an octopus have?")
        print("a) 5")
        print("b) 3")
        print("c) 8")

        equestion2 = input("Your answer:")
        if equestion2 == "c" :
            print("Correct, let's go to the next question.")
            score += 1
        else:
            print("incorrect, next question...")    

        print("Question 3: what is the capital city of England?")
        print("a) Paris")
        print("b) London")
        print("c) Rome")

        equestion3 = input("Your answer:")
        if equestion3 == "b" :
            print("Correct, end of quiz.")
            score += 1
        else:
            print("incorrect, end of quiz")
        
        total_questions = 3
        print(f"Thanks {name} for playing! Your total score was: {score} / {total_questions}")


    elif level == "M":
        print("you chose medium level, great! Let's get started.")

        print("Question 1: how many letters in the alphabet?")
        print("a) 20")
        print("b) 30")
        print("c) 26")

        mquestion1 = input("Your answer:")
        if mquestion1 == "c" :
            print("Correct, next question")
            score += 1
        else:
            print("incorrect, next question")


        print("Question 1: how many sides on a hexagon?")
        print("a) 8")
        print("b) 5")
        print("c) 6")

        mquestion2 = input("Your answer:")
        if mquestion2 == "c" :
            print("Correct, next question")
            score += 1
        else:
            print("incorrect, next question")

        print("Question 1: what colour does blue and yellow make?")
        print("a) orange")
        print("b) green")
        print("c) light blue")

        mquestion3 = input("Your answer:")
        if mquestion3 == "b" :
            print("Correct, end of quiz.")
            score += 1
        else:
            print("incorrect, end of quiz.")

        total_questions = 3
        print(f"Thanks {name} for playing! Your total score was: {score} / {total_questions}")



    elif level == "H":
        print("you chose hard level, great! Let's get started.")

        print("Question 1: what is pythagoras theorem?")
        print("a) a^2 + b^2 = c^2")
        print("b) e = mc^2")
        print("c) (b x h)/2")

        hquestion1 = input("Your answer:")
        if hquestion1 == "a" :
            print("Correct, next question")
            score += 1
        else:
            print("incorrect, next question")


        print("Question 1: what is the population of London?")
        print("a) 9.8 million")
        print("b) 8.4 million")
        print("c) 9.1 million")

        hquestion2 = input("Your answer:")
        if hquestion2 == "a" :
            print("Correct, next question")
            score += 1
        else:
            print("incorrect, next question")

        print("Question 1: who won the world cup in 2010")
        print("a) Germany")
        print("b) Italy")
        print("c) Spain")

        hquestion3 = input("Your answer:")
        if hquestion3 == "c" :
            print("Correct, end of quiz.")
            score += 1
        else:
            print("incorrect, end of quiz.")

        total_questions = 3
        print(f"Thanks {name} for playing! Your total score was: {score} / {total_questions}")

    else:
        print("Sorry, I didn't recognise that level. Please choose E, M, or H.")

while True:
    run_quiz()
    play_again = input("Play again? (y/n)")

    if play_again not in {"y"} :
        print("Thanks for playing, goodbye!✌️")
        break







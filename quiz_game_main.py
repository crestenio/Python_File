import time

print("\nWelcome to Quiz game by STACKTREK CODECAMP!\n")
name = input("Please enter your name: ")
time.sleep(2)
print(f"Hello, {name} welcome to the educational quiz. Here are the questions.")
time.sleep(3)

# main game function


def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("--------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


# play_loop if the user want to play again

def play_again():
    response = input("Do You want to play again? y = yes, n = no \n")
    while response not in ["y", "n", "Y", "N"]:
        response = input("Do You want to play again? y = yes, n = no \n")
    if response == "y":
        new_game()
    elif response == "n":
        print("Thanks For Playing!")
        exit()

# check answer if correct or wrong


def check_answer(answer, guess):

    if answer.lower() == guess.lower():
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# To display the score, print the results and guesses


def display_score(correct_guesses, guesses):
    print("-------")
    print("RESULTS")
    print("-------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print(f" Your score is: {score} %")


questions = {
    "who created python? ": "A",
    "When was python created? ": "B",
    "Where was python name derived from? ": "C"
}

options = [["A. Guido van Rossum", "B. Elon Musk",
            "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. May 5, 1989", "B. February 20, 1991",
            "C. January 8, 2000", "D. June 2, 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"]]


new_game()
play_again()

# end----------------------------------------------------------------------------

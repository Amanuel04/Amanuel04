def main():
    print("Guess the Animal!")
    global score
    score = 0

    guess1 = input("Which bear lives at the North Pole? ").lower()
    question_answer(guess1, 'polar bear')

    guess2 = input("Which is the fastest Land animal? ").lower()
    question_answer(guess2, 'cheetah')

    guess3= input("Which is the largest animal? ")
    question_answer(guess3, "rhinoceros")

    print("Your Score is " + str(score))




def question_answer(guess, name):
    global score
    attempt = 0
    still_guessing = True
    while still_guessing and attempt<3:
        if guess == name:
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry wrong answer. Try again. ").lower()
            attempt = attempt + 1

    if attempt == 3:
        print("The correct answer is " + name)
                



if __name__ == "__main__":
    main()

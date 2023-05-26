import random

numDigits = 3
numGuess = 10

def getSecretNum():
    num = ''
    for i in range(numDigits):
        num+=str(random.randrange(10))

    return num

def giveClue(guessNum,secretNum):
        ans = []

        if guessNum == secretNum:
            ans.append("You got it")
            return ans
        else:
            index = 0 # to check
            for i in guessNum:
                
                indexTwo = 0
                for j in secretNum:
                    if i == j:
                        if index == indexTwo:
                            ans.append('Fermi')
                            continue
                        else:
                            ans.append('Pico')
                            continue
                    indexTwo+=1
                index+=1

        if len(ans) == 0:
                ans.append('Bagels')

        return ans

            

            
def main():
    print("""
            Bagels is a deductive logic game where you must guess a number
        based on clues.

        I am thinking of a {} digit number with no repeated digits.
        Try to guess what it is.
        The clues are:

        Pico     means One digit is correct but in the wrong position.
        Fermi    means One digit is correct and in the right position.
        Bagels   means No digit is correct. 

        For example if the secret number was 248 and your guess was 843, the
        clue would be Fermi Pico.
    """.format(numDigits))
    
    while True:
        secretNum = getSecretNum()
        print("I have a {} digit number.".format(numDigits))
        
        
        numGuess = 1

        while numGuess <= 10:
             
             print("Guess #{}".format(numGuess))
             guessNum = input('> ')
             if len(guessNum) == 3 or len(guessNum) == 2:
                if len(guessNum) == 2:
                     gueessNum = '0' + guessNum

                clue = giveClue(guessNum,secretNum)
                
                if clue[0] == "You got it":
                    print(clue)
                    break
                else:
                    print(clue)
                    numGuess+=1

        if numGuess > 10:
            print("The secret Number is: ", secretNum)
        question = input("Would you like to play again? Y/n").lower()
        if question != 'y':
            break

    print("Thank You for Playing!")

    





if __name__ == '__main__':
    main()
            

    

import random
import string

adjectives = ['sleepy', 'slow', 'smelly',
                'wet', 'fat', 'red',
              'orange', 'yellow', 'green',
              'blue', 'purple', 'fluffy',
              'white','proud', 'brave'
              ]
nouns= [
    'apple', 'dinosaur','ball',
    'toaster','goat','dragon',
    'hammer', 'duck', 'panda'
    ]

print("Welcome to Password Picker!")

while True:
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    number = random.randint(0,100)
    special_char = random.choice(string.punctuation)

    password = adjective + noun + str(number) + special_char
    print("your new password is: %s" %password)

    response = input("Would you like another password? ).lower()
    if response == 'n':
        print("You're welcome")
        break

import random

decks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']


def hit():
        x = random.choice(decks)
        if x == 'A':
            if player < 11:
                return 11
            else:
                return 1
        elif x in ["J","Q","K"]:
            return 10
        else:
            return int(x)

while True:
    dealer = 0
    player = 0

    dealerCards = []
    playerCards = []

    firstHitD= hit()
    dealer += firstHitD
    dealerCards.append(firstHitD)
    
    firstHitP = hit()
    player += firstHitP
    playerCards.append(firstHitP)

    print("You got", player)
    
     
    while player <= 21:
        move = input("> hit or stand").lower()

        if move == "h":
            hitP = hit()
            player += hitP
            playerCards.append(hitP)

            for i in playerCards:
                print(i)
        elif move == "s":
            break

    while dealer <= 21:
        if player > 21:
            print("You Lost")
            break

        hitD = hit()
        dealer += hitD
        dealerCards.append(hitD)
        for i in dealerCards:
            print(i)

        if dealer <= 21 and dealer > player:
            print("You lost")
            break
        elif dealer > 21:
            print("You won")

        
        

    continuePlaying = input("Play Again? Y/n").lower()
    if continuePlaying == "n":
        break

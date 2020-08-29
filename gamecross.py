import random

word = "shruti"
guess = random.sample(range(0,len(word)),3)
guesses = ""
for i in guess:
    guesses += word[i]
count = 5
play = "Yes"


def playagain():
    global play
    play = input("Do you want to paly again(Yes/No) :")
    if play == "Yes":
        print("Its working")
        global count,guesses,guess,word
        guess = random.sample(range(0, len(word)), 3)
        guesses = ""
        for i in guess:
            guesses += word[i]
        count = 5


while play =="Yes":
    while count>0:
        won = True
        for i in word:
            if i in guesses:
                print(f"{i}",end=" ")
            else:
                print("_",end=" ")
                won = False


        if won == True:
            print(f"\n You Won \n Score : {count*10}")
            playagain()
            break

        x = input("\nEnter a letter")
        guesses += x

        if x not in word:
            count -= 1
            print(f"{count} Chances Left !!")

            if count == 0:
                print("You Loose")
                playagain()
                break

print("Thanks for playing!!")
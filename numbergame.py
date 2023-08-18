import random
a=random.randint(1,20)
print("HI PLAYER 🙏\n")
print("Guess a number between 1 to 20😎\n")
for i in range(5):
    p=int(input("Enter your choice:\n"))
    if(a==p):
        print("YOU GUESSED RIGHT😱!\n")
        break
    elif(p>a):
        print("NUMBER IS HIGH 😨\n")
    else:
        print("NUMBER IS LOW GUESS AGAIN 😢\n")
    print("YOUR REMAINING GUESSES:😉\n",4-i)   
print("THE CORRECT NUMBER IS:😇\n",a)    
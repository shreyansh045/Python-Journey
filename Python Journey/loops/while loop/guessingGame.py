import random
num= random.randint(1,10)
tries=0
while True:
    guess=int(input("Guess the number between 1 and 10:"))

    if num==guess:
        tries+=1
        print(f"You are right you guessed the number in {tries} tries")
        break

    elif num>guess:
        tries+=1
        print("Go to little higher")
    
    elif num<guess:
        tries+=1 
        print("Go to little lower")
    
    else:
        tries+=1
        print("Sorry you are wrong")

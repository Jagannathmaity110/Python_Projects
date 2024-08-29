import random  ## we just import the random module

number = random.randint(1,100)
attempts = 0

while True:
    guess = int(input("Guess the number between 1 to 100")) ## Here you use input function to take input from user

    attempts+=1
    if guess >number:
        print("Your guess is too high")
    elif guess <  number :
        print("Your guess is too low")
    else:
        print(f"You guess the number correctly in {attempts}")
        break
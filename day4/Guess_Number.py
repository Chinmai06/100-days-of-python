import random
print("Welcome to the Guess the number Game. to win, you must guess the two digit number that I am thinking of.")
random_number=random.randint(10,99)
number_the_user_guess=int(input("Guess the number: "))
if number_the_user_guess==random_number:
    print("Congratulations! YOU WIN!")
elif number_the_user_guess>random_number:
    print(f"Too high. Try again. {random_number}")
elif number_the_user_guess<random_number:
    print(f"Too low. Try again. {random_number}")
print("Game over.")

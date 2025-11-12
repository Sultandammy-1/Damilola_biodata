# Question 2 - Guess the number
secret_number = 7
guess=int(input("Guess the number: "))
while guess!=secret_number:
    print("Wrong, try again.")
    guess=int(input("Guess the number: "))
else:
    print("Correct!")

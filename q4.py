# Question 4 - Password prompt
correct_password="python123"
password=input("Enter password: ")
while password!=correct_password:
    print("Wrong Password, try again.")
    password=input("Enter password: ")
else:
    print("Password accepted!")
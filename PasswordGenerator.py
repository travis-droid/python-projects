import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

try:
    length = int(input("Enter the password length: "))
    if length < 5:
        print("Too short! Please enter at leat 8+ charaters.")
    else:
        password = generate_password(length)
        print(f"Your stong password is: {password}")
except ValueError:
    print("Please Enter a valid number for the password!")
#the below code is not correct!
#while True:
#    generate_password(length)
#    choice = input("Do you want to generate another password? (yes/no): ")
#    if choice.lower()!= 'yes':
#        break
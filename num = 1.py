num = 1

while num <= 1000:
    if num % 3 == 0:
        print(num)
    num += 1

# This script prints all numbers from 1 to 1000 that are divisible by 3.

while True:
    inches = float(input("Enter inches (negative number to quit): "))
    
    if inches < 0:
        print("Program ended.")
        break
    
    centimeters = inches * 2.54
    print(inches, "inches =", centimeters, "cm")


# This script converts inches to centimeters until a negative number is entered.

numbers = []

while True:
    user_input = input("Enter a number (press Enter to quit): ")
    
    if user_input == "":
        break
    
    numbers.append(float(user_input))

if numbers:
    print("Smallest:", min(numbers))
    print("Largest:", max(numbers))
else:
    print("No numbers were entered.")

# This script collects numbers from the user and then displays the smallest and largest numbers entered.

import random

secret_number = random.randint(1, 10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Correct!")
        break


# This script is a number guessing game where the user tries to guess a randomly selected number between 1 and 10.

correct_username = "python"
correct_password = "rules"

attempts = 0

while attempts < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        print("Incorrect credentials")
        attempts += 1

if attempts == 5:
    print("Access denied")

# This script allows a user to log in with a username and password, giving them up to 5 attempts.

def middle_char(text):
    length = len(text)
    mid = length // 2
    
    if length % 2 == 0:
        return text[mid - 1: mid + 1]
    else:
        return text[mid]



def make_acronym(phrase):
    words = phrase.split()
    acronym = ""
    
    for word in words:
        acronym += word[0].upper()
    
    return acronym

# This code defines two functions: one to get the middle character(s) of a string and another to create an acronym from a phrase.

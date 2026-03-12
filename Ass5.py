import re
import random

# Question 1
# Function to check if a course code is valid
def check_course_code(code):
    pattern = r'^[A-Z]{2,3}\d{3}$'
    if re.match(pattern, code):
        return True
    else:
        return False


# Question 2
# Function to check if a hex color is valid
def check_hex_color(color):
    pattern = r'^#[0-9A-Fa-f]{6}$'
    if re.match(pattern, color):
        return True
    else:
        return False


# Question 3
# Find all numbers in a paragraph and calculate the sum
def sum_numbers(text):
    nums = re.findall(r'\d+', text)
    total = 0
    for n in nums:
        total += int(n)
    return total


# Question 4
# Hide phone numbers
def hide_phone(text):
    pattern = r'(\+84\d+|\b\d{10}\b)'
    result = re.sub(pattern, "[REDACTED]", text)
    return result


# Question 5
# Approximate value of pi using random points
def approximate_pi(n):
    inside = 0

    for i in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x*x + y*y < 1:
            inside += 1

    pi = 4 * inside / n
    return pi


# -------- Main program --------

# Test course code
code = input("Enter a course code: ")
print("Valid course code:", check_course_code(code))


# Test hex color
color = input("Enter a hex color: ")
print("Valid hex color:", check_hex_color(color))


# Test number sum
text = input("Enter a paragraph: ")
print("Sum of numbers:", sum_numbers(text))


# Test hiding phone numbers
doc = input("Enter text with phone numbers: ")
print("After hiding numbers:", hide_phone(doc))


# Pi approximation
points = int(input("How many random points to generate? "))
pi_value = approximate_pi(points)
print("Approximate value of pi:", pi_value)



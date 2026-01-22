# EX1 – Zander length
length = float(input("Enter the length of the zander in centimeters: "))

if length < 42.0:
    missing = 42.0 - length
    print("Throw the small zander back.")
    print(f"The fish is lacking {missing:.1f} cm to be able to pass.")
else:
    print("The zander can be caught.")

# EX2 – Cruise ship cabin class
cabin_class = input("Enter your cabin class of the cruise ship: ").upper()

if cabin_class == "LUX":
    print("LUX: upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("A: above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("B: windowless cabin above the car deck.")
elif cabin_class == "C":
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

# EX3 – Hemoglobin level
def hemoglobin_level():
    try:
        gender = input("Enter biological sex (female/male): ").lower()
        hemoglobin = float(input("Enter hemoglobin value (g/l): "))

        if gender == "female":
            if hemoglobin < 117:
                print("Hemoglobin level is low.")
            elif hemoglobin <= 155:
                print("Hemoglobin level is normal.")
            else:
                print("Hemoglobin level is high.")

        elif gender == "male":
            if hemoglobin < 134:
                print("Hemoglobin level is low.")
            elif hemoglobin <= 167:
                print("Hemoglobin level is normal.")
            else:
                print("Hemoglobin level is high.")
        else:
            print("Invalid biological sex entered.")

    except ValueError:
        print("Please enter a valid number for hemoglobin.")

hemoglobin_level()


# EX4 – Leap year checker
def check_leap_year():
    try:
        year = int(input("Enter a year: "))

        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")

    except ValueError:
        print("Please enter a valid year.")

check_leap_year()


# EX5 – Pizza value comparison
import math

def unit_price_pizza(diameter_cm, price_usd):
    diameter_m = diameter_cm / 100
    radius_m = diameter_m / 2
    area = math.pi * radius_m ** 2
    return price_usd / area

d1 = float(input("Enter diameter of pizza 1 (cm): "))
p1 = float(input("Enter price of pizza 1 (USD): "))

d2 = float(input("Enter diameter of pizza 2 (cm): "))
p2 = float(input("Enter price of pizza 2 (USD): "))

price1 = unit_price_pizza(d1, p1)
price2 = unit_price_pizza(d2, p2)

print(f"Pizza 1 unit price: {price1:.2f} USD/m²")
print(f"Pizza 2 unit price: {price2:.2f} USD/m²")

if price1 < price2:
    print("Pizza 1 provides better value for money.")
elif price2 < price1:
    print("Pizza 2 provides better value for money.")
else:
    print("Both pizzas have the same value for money.")

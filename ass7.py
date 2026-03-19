import random

# Car class
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    # Accelerate method
    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        if self.current_speed < 0:
            self.current_speed = 0

    # Drive method
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


# ---------------- MAIN PROGRAM ----------------

# Part 1: Create one car
car = Car("ABC-123", 142)

print("Initial Car Info:")
print(f"Registration: {car.registration_number}")
print(f"Max Speed: {car.max_speed} km/h")
print(f"Current Speed: {car.current_speed} km/h")
print(f"Distance: {car.travelled_distance} km")


# Part 2: Test accelerate
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)

print("\nSpeed after acceleration:", car.current_speed, "km/h")

# Emergency brake
car.accelerate(-200)
print("Speed after emergency brake:", car.current_speed, "km/h")


# Part 3: Test drive
car.current_speed = 60
car.travelled_distance = 2000

car.drive(1.5)
print("\nDistance after driving:", car.travelled_distance, "km")


# Part 4: Car race

cars = []

# Create 10 cars
for i in range(10):
    reg = f"ABC-{i+1}"
    max_speed = random.randint(150, 200)
    cars.append(Car(reg, max_speed))

hours_passed = 0

# Race loop
while True:
    hours_passed += 1

    for car in cars:
        change = random.randint(-10, 15)
        car.accelerate(change)
        car.drive(1)

    # Check if any car reached 10,000 km
    if any(car.travelled_distance >= 10000 for car in cars):
        break


# Print results
print("\n--- Race Results ---")
print(f"Race finished in {hours_passed} hours\n")

print(f"{'Car':<10} {'MaxSpeed':<10} {'Speed':<10} {'Distance':<10}")
for car in cars:
    print(f"{car.registration_number:<10} {car.max_speed:<10} {car.current_speed:<10} {round(car.travelled_distance, 2):<10}")
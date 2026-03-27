import random

# ----------------------
# Elevator Class
# ----------------------
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom = bottom_floor
        self.top = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"Elevator at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator at floor {self.current_floor}")

    def go_to_floor(self, target):
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()


# ----------------------
# Building Class
# ----------------------
class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []

        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator_number, destination):
        print(f"\nRunning elevator {elevator_number} to floor {destination}")
        self.elevators[elevator_number].go_to_floor(destination)

    def fire_alarm(self):
        print("\n🔥 FIRE ALARM ACTIVATED! 🔥")
        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i} going to bottom floor")
            elevator.go_to_floor(self.bottom)


# ----------------------
# Car Class
# ----------------------
class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0

    def drive(self, hours):
        self.distance += self.current_speed * hours


# ----------------------
# Race Class
# ----------------------
class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.current_speed = max(0, min(car.max_speed, car.current_speed + change))
            car.drive(1)

    def print_status(self):
        print("\n--- Race Status ---")
        print(f"{'Car':10} {'Speed':10} {'Distance':10}")
        for car in self.cars:
            print(f"{car.reg_number:10} {car.current_speed:10} {car.distance:10}")

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False


# ----------------------
# MAIN PROGRAM
# ----------------------
if __name__ == "__main__":

    # 🔹 Elevator Test
    print("=== Elevator Test ===")
    h = Elevator(1, 10)
    h.go_to_floor(5)
    h.go_to_floor(1)

    # 🔹 Building Test
    print("\n=== Building Test ===")
    building = Building(1, 10, 3)

    building.run_elevator(0, 7)
    building.run_elevator(1, 5)

    building.fire_alarm()

    # 🔹 Race Simulation
    print("\n=== Race Simulation ===")

    cars = []
    for i in range(10):
        cars.append(Car(f"ABC-{i+1}", random.randint(100, 200)))

    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0
    while not race.race_finished():
        race.hour_passes()
        hours += 1

        if hours % 10 == 0:
            race.print_status()

    print("\n🏁 Race Finished!")
    race.print_status()
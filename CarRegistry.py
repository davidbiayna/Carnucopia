from Car import Car
import csv
import pdb
from tabulate import tabulate


class CarRegistry:

    def __init__(self):
        self._hire_out = None
        self._cars = []
        self._headers = ["Pos", "ID", "Reg", "Manufacturer", "Model", "SIPP", "Seat", "Width", "Length", "Spd", "MPG",
                         "OnHire"]

    def set_file_headers(self):
        try:
            filename = "C:\\Temp\\CarRegistry.dat"

            # Read existing data
            with open(filename, "r", newline='') as file:
                existing_data = list(csv.reader(file))

            updated_data = [self._headers] + existing_data
            # pdb.set_trace()
            # Write the updated data back to the file that now contains both headers and data
            with open(filename, "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(updated_data)

        except FileNotFoundError:
            print("CarRegistry.dat file not found")

    def add_pos_value(self):
        filename = "C:\\Temp\\CarRegistry.dat"

        # Read existing data
        with open(filename, "r", newline='') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)
            rows = list(csv_reader)

        # Update 'Pos' column starting from 1 (skip header)
        for i, row in enumerate(rows, start=1):
            row.insert(0, str(i))

        # Combine headers and updated rows
        updated_data = [headers] + rows

        # Re-write the updated data to the file
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(updated_data)

    def set_cars_data(self, headers, rows):
        self._cars = {f'car_{i}': dict(zip(headers, row)) for i, row in enumerate(rows, start=1)}
        # pdb.set_trace()
        self._cars

    def get_cars(self):
        return self._cars

    def find_car(self, car_id):
        for car in self._cars:
            if car.registration_plate == car_id:
                return car
        return None

    @property
    def cars(self):
        return self._cars

    @property
    def number_of_cars(self):
        return len(self._cars)

    def display_car_registry_state(self):
        print("Current state of CarRegistry:")
        print(tabulate(self._cars.values(), headers='keys', tablefmt="plain"))

    def add_car(self, car):
        if isinstance(car, Car):
            if car in self._cars:
                print(f"{car.registration_plate} is already in the registry")
            else:
                self._cars.append(car)
                print(f"{car.registration_plate} added to registry")
                self.display_car_registry_state()
                self.save_registry_to_file()

    def remove_car(self):
        pos = self.receive_position_number()
        try:
            selected_car = self._cars[f"car_{pos}"]
            print(f"Car found: {selected_car['Manufacturer'], selected_car['Reg']}")
        except IndexError:
            print("Invalid position number. No car found.")
        confirmation = self.confirm_action("Are you sure you want to delete this car? (Y/N)")
        if confirmation:
            self.remove_car_by_position(pos)
            print("Car deleted successfully.")
        else:
            print("Deletion canceled.")

    def confirm_action(self, message: str) -> bool:
        response = input(f"{message} (Y/N)").upper()
        while response not in {'Y', 'N'}:
            print("Invalid response. Please enter 'Y' or 'N'.")
            response = input(f"{message} (Y/N)").upper()

        return response == 'Y'

    def receive_position_number(self) -> int:
        pos = int(input("Enter Position Number: "))
        return pos

    def remove_car_by_position(self, pos):
        if 1 <= pos <= len(self._cars):
            selected_car = self._cars[f"car_{pos}"]
            self._cars.pop(f"car_{pos}")
            print(f"Car {selected_car['Reg']} removed from the registry")
            self.display_car_registry_state()
        else:
            print("Invalid position number")

    def return_car_to_garage(self, car_id):
        for car in self._cars:
            if car.car_id == car_id:
                if not car.on_hire:
                    return f"Sorry, the car registered as {car.registration_plate} is already in the garage"
                else:
                    car.on_hire = False
                    return f"The car registered as {car.registration_plate} has successfully returned to the garage"

        return f"The car with ID of {car_id} is not in the garage"

    @property
    def hire_out(self):
        return self._hire_out

    @hire_out.setter
    def hire_out(self, car_id):
        car = self.find_car(car_id)

        if not car:
            print(f" Sorry, the car {car_id} is not in the registry")
            return
        if car.hire_out:
            print(f"{car.registration_plate} is already out on hire")
        else:
            car.hire_out = True
            print(f"{car.registration_plate} is now out on hire")
            self.display_car_registry_state()

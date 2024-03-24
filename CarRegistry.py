import pdb

from Car import Car
import csv
from tabulate import tabulate

class CarRegistry:

    def __init__(self):
        self._cars = {}
        self._car = Car
        self.initial_file_rows = []
        self._prettyfied_cars = {}
        self._car_attrs = {'Pos': 'pos_id', 'ID': 'car_id', 'Reg': 'registration_plate', "Manufacturer": 'manufacturer',
                           "Model": 'model_type', "SIPP": 'sipp', "Seat": 'seat_capacity',
                           "Width": 'width', "Length": 'length', "Spd": 'maximum_speed',
                           "MPG": 'mpg', "OnHire": 'on_hire'}

    def set_file_headers_and_pos_values(self):
        try:
            filename = "C:\\Temp\\CarRegistry.dat"

            # Read existing data
            with open(filename, "r", newline='') as file:
                existing_data = list(csv.reader(file))
                if existing_data[0] == list(self._car_attrs.keys()):
                    # If headers match, exclude the header row
                    self._initial_file_rows = existing_data[1:]
                else:
                    self._initial_file_rows = existing_data
            # Check if headers already exist  so we do not duplicate the headers rows
            if existing_data[0] == list(self._car_attrs.keys()):
                return

            # Adds the pos value starting with 1

            for i, row in enumerate(existing_data, start=1):
                row.insert(0, str(i))
            updated_data = [self._car_attrs.keys()] + existing_data
            # Writes the data back to the file that now contains both headers and data
            with open(filename, "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(updated_data)
        except FileNotFoundError:
            print("CarRegistry.dat file not found.")

    def set_cars_data(self):
        headers = self._car_attrs.keys()
        file_rows = {f'car_{i}': dict(zip(headers, row)) for i, row in enumerate(self._initial_file_rows, start=1)}
        for key, value in file_rows.items():
            car_data = {}
            for header, attr in zip(headers, value):
                attribute_name = self._car_attrs.get(header)
                if attribute_name:
                    car_data[attribute_name] = value[header]
            car = Car(pos_id=car_data['pos_id'],
                      car_id=car_data['car_id'],
                      registration_plate=car_data['registration_plate'],
                      manufacturer=car_data['manufacturer'],
                      model_type=car_data['model_type'],
                      sipp=car_data['sipp'],
                      seat_capacity=car_data['seat_capacity'],
                      width=car_data['width'],
                      length=car_data['length'],
                      maximum_speed=car_data['maximum_speed'],
                      mpg=car_data['mpg'],
                      on_hire=car_data['on_hire'])
            self._cars[f"car_{car.pos_id}"] = car
            # example of how the cars data structure gets created:
            # {'car_1': {'pos_id': '1', 'car_id': '1', 'registration_plate': 'BD61 SLU',
            # 'manufacturer': 'HONDA',
            # 'model_type': 'CR-V', 'sipp': 'SFDR',
            # 'seat_capacity': '5', 'width': '1780', 'length': '4510', 'maximum_speed': '130',
            #  'mpg': '39', 'on_hire': 'True'}
            self.update_cars_registry()

    def update_cars_registry(self):
        reversed_headers = {v: k for k, v in self._car_attrs.items()}
        for car_id, car_obj in self._cars.items():
            car_attrs = {}
            for attr_name, attr_value in vars(car_obj).items():
                header_key = attr_name[1:] if attr_name.startswith('_') else attr_name
                car_attrs[reversed_headers[header_key]] = attr_value
            self._prettyfied_cars[car_id] = car_attrs

    @property
    def cars(self):
        return self._cars

    def display_car_registry_state(self):
        print("Current state of CarRegistry:")
        data = self._prettyfied_cars
        print(tabulate(data.values(), headers='keys', tablefmt="plain", showindex="plain"))

    def save_registry_to_file(self):
        filename = "C:\\Temp\\CarRegistry.dat"
        current_cars_state = self._prettyfied_cars
        headers = list(current_cars_state[next(iter(current_cars_state))].keys())
        rows = [list(car_data.values()) for car_data in current_cars_state.values()]
        # Re-write the updated data to the file
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(rows)

    def add_car(self):
        # Calculate the new car ID
        new_car_id = max(int(car.car_id) for car in self._cars.values()) + 1 if self._cars else 1

        while True:
            # Retrieve the user input for tthe new car
            registration_plate = input("Enter Registration Plate: ")
            if registration_plate.upper() == 'Q':
                print("Returning to main menu...")
                return

            manufacturer = input("Enter Manufacturer: ")
            if manufacturer.upper() == 'Q':
                print("Returning to main menu...")
                return

            model_type = input("Enter Model/Type: ")
            if model_type.upper() == 'Q':
                print("Returning to main menu...")
                return

            sipp = input("Enter SIPP code: ")
            if sipp.upper() == 'Q':
                print("Returning to main menu...")
                return

            seat_capacity_input = input("Enter Seat Capacity: ")
            if seat_capacity_input.upper() == 'Q':
                print("Returning to main menu...")
                return
            try:
                seat_capacity = int(seat_capacity_input)
            except ValueError:
                print("Invalid input. Please enter a number or Q to return to main menu")
                continue

            width_input = input("Enter Width: ")
            if width_input.upper() == 'Q':
                print("Returning to main menu...")
                return
            try:
                width = int(width_input)
            except ValueError:
                print("Invalid input. Please enter a number or Q to return to main menu")
                continue

            length_input = input("Enter Length: ")
            if length_input.upper() == 'Q':
                print("Returning to main menu...")
                return
            try:
                length = int(length_input)
            except ValueError:
                print("Invalid input. Please enter a number or Q to return to main menu")
                continue

            maximum_speed_input = input("Enter Maximum Speed: ")
            if maximum_speed_input.upper() == 'Q':
                print("Returning to main menu...")
                return
            try:
                maximum_speed = float(maximum_speed_input)
            except ValueError:
                print("Invalid input. Please enter a number or Q to return to main menu")
                continue

            mpg_input = input("Enter MPG: ")
            if mpg_input.upper() == 'Q':
                print("Returning to main menu...")
                return
            try:
                mpg = float(mpg_input)
            except ValueError:
                print("Invalid input. Please enter a number or Q to return to main menu")
                continue

            on_hire = input("Enter On Hire Status (T/F): ")
            if on_hire.upper() == 'Q':
                print("Returning to main menu...")
                return
            elif on_hire.upper() not in ['T', 'F']:
                print("Invalid input. Please enter a number or Q to return to main menu")
                continue

            car = Car(pos_id=len(self._cars) + 1,
                      car_id=new_car_id,
                      registration_plate=registration_plate,
                      manufacturer=manufacturer,
                      model_type=model_type,
                      sipp=sipp,
                      seat_capacity=seat_capacity,
                      width=width,
                      length=length,
                      maximum_speed=maximum_speed,
                      mpg=mpg,
                      on_hire=on_hire)
            if car.is_valid(car):
                self._cars[f"car_{car.pos_id}"] = car
                self.update_state_of_cars_table_and_file()
                print("Car object created successfully!")
                return
            else:
                print('Please see above validation errors and try again with correct input')

    def remove_car(self):
        pos = self.receive_position_number()
        try:
            selected_car = self._cars[f"car_{pos}"]
            print(f"Car found: {selected_car.manufacturer, selected_car.registration_plate}")
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
            self._prettyfied_cars.pop(f"car_{pos}")
            print(f"Car {selected_car.registration_plate} removed from the registry")
            self.update_state_of_cars_table_and_file()
        else:
            print("Invalid position number")

    def return_car_to_garage(self):
        pos = self.receive_position_number()
        try:
            selected_car = self._cars[f"car_{pos}"]
            print(f"Car found: {selected_car.manufacturer, selected_car.registration_plate}")
        except IndexError:
            print("Invalid position number. No car found.")
            return

        if selected_car.on_hire:
            confirmation = self.confirm_action("Are you sure you want to return this car to the garage? (Y/N)")
            if confirmation:
                self._cars[f"car_{pos}"].on_hire = False
                print("Car returned successfully.")
                self.update_state_of_cars_table_and_file()
            else:
                print("Return canceled.")
        else:
            print(f"Sorry, the car registered as {selected_car.registration_plate} is already in the garage!")

    def hire_out(self):
        pos = self.receive_position_number()
        try:
            selected_car = self._cars[f"car_{pos}"]
            print(f"Car found: {selected_car.manufacturer}, {selected_car.registration_plate}")
        except IndexError:
            print(f"Invalid position number. No car found.")
        if selected_car.on_hire == True:
            print(f"Sorry, the car registered as {selected_car.registration_plate} is already out on hire!")
        else:
            confirmation = self.confirm_action("Are you sure you want to hire out this car? (Y/N)")
            if confirmation:
                selected_car.on_hire = True
                print(f"Car registered as {selected_car.registration_plate} is now out on hire.")
                self.update_state_of_cars_table_and_file()
            else:
                print("Hire out canceled.")

    def update_state_of_cars_table_and_file(self):
        self.update_cars_registry()
        self.display_car_registry_state()
        self.save_registry_to_file()

    def update_registry(self):
        self.update_state_of_cars_table_and_file()
        print('The registry has been successfully updated!')

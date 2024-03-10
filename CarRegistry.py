from Car import Car
import csv
import pdb
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
                self._initial_file_rows = existing_data
            # Check if headers already exist so we do not duplicate the headers rows
            if existing_data and existing_data[0] == self._car_attrs.keys():
                return

            for i, row in enumerate(existing_data, start=1):
                row.insert(0, str(i))
            updated_data = [self._car_attrs.keys()] + existing_data

            # Writes the data back to the file that now contains both headers and data
            with open(filename, "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(updated_data)

        except FileNotFoundError:
            print("CarRegistry.dat file not found.")

    # def set_cars_data(self, headers, rows):
        # self._cars = {f'car_{i}': dict(zip(headers, row)) for i, row in enumerate(rows, start=1)}
        # self.create_cars_with_attrs()

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
            self._cars[f"car_{car.car_id}"] = car

        reversed_headers = {v: k for k, v in self._car_attrs.items()}
        for car_id, car_obj in self._cars.items():
            car_attrs = {}
            for attr_name, attr_value in vars(car_obj).items():
                header_key = attr_name[1:] if attr_name.startswith('_') else attr_name
                car_attrs[reversed_headers[header_key]] = attr_value
            self._prettyfied_cars[car_id] = car_attrs

    def get_cars(self):
        return self._cars

    @property
    def cars(self):
        return self._cars

    @property
    def number_of_cars(self):
        return len(self._cars)

    def display_car_registry_state(self):
        print("Current state of CarRegistry:")
        data = self.car_registry._prettyfied_cars
        print(tabulate(data.values(), headers='keys', tablefmt="plain"))

    def save_registry_to_file(self, data):
        # filename = "C:\\Temp\\CarRegistry.dat"
        headers = self._car_attrs.keys()
        pdb.set_trace()
        rows = [[str(car['Pos'])] + [str(car[key]) for key in list(headers)[1:]] for car in data.values()]

        # Re-write the updated data to the file
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(rows)

    def add_car(self):
        incoming_car_to_be_added_to_the_file = self.retrieve_car_details()
        self._cars.update(incoming_car_to_be_added_to_the_file)
        print("Car successfully added")
        self.display_car_registry_state()
        self.save_registry_to_file(self._cars)

    def retrieve_car_details(self):
        car_attributes = {}
        car_instance = Car()  # Instantiate the Car class

        # Retrieve the next available ID
        car_instance.pos_id = len(self._cars) + 1
        car_attributes.update({'Pos': self.pos_id})

        # Retrieve the next available position ID
        car_instance.car_id = max(int(car['ID']) for car in self._cars.values()) + 1
        car_attributes.update({'ID': self.car_id})

        car_instance.registration_plate = str(input("Enter Registration Plate: "))
        car_attributes.update({'Reg': car_instance.registration_plate})

        car_instance.manufacturer = str(input("Enter Manufacturer: "))
        car_attributes.update({'Manufacturer': car_instance.manufacturer})

        car_instance.model_type = str(input("Enter Model/Type: "))
        car_attributes.update({'Model': car_instance.model_type})

        car_instance.sipp = str(input("Enter SIPP code: "))
        car_attributes.update({'SIPP': car_instance.sipp})

        seat_capacity_value = car_instance.set_seat_capacity(int(input("Enter Seat Capacity: ")))
        car_attributes.update({'Seat': seat_capacity_value})

        car_instance.width = int(input("Enter Width: "))
        car_attributes.update({'Width': car_instance.width})

        car_instance.length = int(input("Enter Length: "))
        car_attributes.update({'Length': car_instance.length})

        car_instance.maximum_speed = float(input("Enter Maximum Speed: "))
        car_attributes.update({'Spd': car_instance.maximum_speed})

        car_instance.mpg = float(input("Enter MPG: "))
        car_attributes.update({'MPG': car_instance.mpg})

        car_instance.on_hire = bool(input("Enter On Hire Status (T/F): "))
        car_attributes.update({'OnHire': car_instance.on_hire})

        car_position_id = f"car_{self.pos_id}"
        new_car_hash = {car_position_id: car_attributes}
        return new_car_hash

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
            self.save_registry_to_file(self._cars)
        else:
            print("Invalid position number")

    def return_car_to_garage(self):
        pos = self.receive_position_number()
        try:
            selected_car = self._cars[f"car_{pos}"]
            print(f"Car found: {selected_car['Manufacturer'], selected_car['Reg']}")
        except IndexError:
            return "Invalid position number. No car found."

        if not selected_car["OnHire"]:
            print(f"Sorry, the car registered as {selected_car['Reg']} is already in the garage!")
            return

        confirmation = self.confirm_action("Are you sure you want to return this car to the garage? (Y/N)")
        if confirmation:
            self._cars[f"car_{pos}"].on_hire
            self.display_car_registry_state()
            self.save_registry_to_file(self._cars)
            print("Car returned successfully.")
        else:
            print("Return canceled.")

    def hire_out(self):
        pos = self.receive_position_number()
        try:
            selected_car = self._cars_with_attributes[f"car_{pos}"]
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
                self.display_car_registry_state()
                self.save_registry_to_file(self._cars)
            else:
                print("Hire out canceled.")

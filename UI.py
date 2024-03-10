import csv
import pdb
from Car import Car
from CarRegistry import CarRegistry
from tabulate import tabulate


class UI:

    def __init__(self, car_registry):
        self.car_registry = car_registry
        self.exit_flag = False
        # self.headers = self.display_header()
        # self.rows = self.display_items()
    def sanitize_data(self):
        self.car_registry.set_file_headers_and_pos_values()

    def display_header(self):
        with open("C:\\Temp\\CarRegistry.dat", "r") as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader, None)
            return headers

    def display_items(self):
        cars = []
        try:
            with open("C:\\Temp\\CarRegistry.dat", "r") as file:
                csv_reader = csv.reader(file)
                # Skip headers
                next(csv_reader, None)
                for row in csv_reader:
                    cars.append(row)
        except FileNotFoundError:
            print("No existing registry file found.")
        return cars

    def display_pretty_table(self):
        # Print the table using the data values from the key value pairs and the established headers
        data = self.car_registry._prettyfied_cars
        # Print the table using tabulate
        print(tabulate(data.values(), headers='keys', tablefmt="plain"))

    # def set_cars_data_state(self):
        # Transform each row in a dictionary such as a hash - key value pairs so we can further manipulate the data
        # ex:
        # {'car_1': {'Pos': '1', 'ID': '1', 'Reg': 'BD61 SLU', 'Manufacturer': 'HONDA', 'Model': 'CR-V', 'SIPP': 'SFDR',
        #            'Seat': '5', 'Width': '1780', 'Length': '4510', 'Spd': '130', 'MPG': '39', 'OnHire': 'True'},
        #  'car_2': {'Pos': '2', 'ID': '2', 'Reg': 'CA51 MBE', 'Manufacturer': 'CHEVROLET', 'Model': 'CORVETTE',
        #            'SIPP': 'JTAV', 'Seat': '2', 'Width': '1877', 'Length': '1234', 'Spd': '194', 'MPG': '24',
        #            'OnHire': 'True'}
        # Set the cars data in CarRegistry
        # self.car_registry.set_cars_data(self.headers, self.rows)
        # self.car.update_cars_attributes()
        # Print the table using the data values from the key value pairs and the established headers
        # self.data = {f'car_{i}': dict(zip(headers, row)) for i, row in enumerate(rows, start=1)}
        # print(tabulate(self.data.values(), headers="keys", tablefmt="plain"))

    def display_menu(self):
        print("Menu Options:")
        print("A - Add Car:")
        print("D - Delete Car:")
        print("H - Hire Out Car:")
        print("R - Return Car to Garage:")
        print("U - Update Car Registry:")
        print("X - Exit:")

    def process_options(self):
        while True:
            option = input("Enter your choice: ")

            if option == 'A':
                self.car_registry.add_car()
            elif option == 'D':
                self.car_registry.remove_car()
            elif option == 'H':
                self.car_registry.hire_out()
            elif option == 'R':
                self.car_registry.return_car_to_garage()
            elif option == 'U':
                self.car_registry.update_registry()
            elif option == 'X':
                if self.confirm_exit():
                    self.exit_flag = True
                break
            else:
                print("Invalid option. Please try again")

    def confirm_exit(self) -> bool:
        response = input('Are you sure you want to leave, Y or N').upper()
        while response not in {'Y', 'N'}:
            print("Invalid response. Please enter 'Y or 'N'.")
            response = input('Are you sure you want to leave, Y or N').upper()

        return response == 'Y'

    def hire_out_car(self):
        pos = self.gather_position_number()
        result = self.car_registry.hire_out_car(pos)
        print(result)

    def return_car_to_garage(self):
        pos = self.gather_position_number()
        result = self.car_registry.return_car_to_garage()
        print(result)

    def update_registry(self):
        self.car_registry.update_registry()

    def my_car_registry(self):
        return self.car_registry
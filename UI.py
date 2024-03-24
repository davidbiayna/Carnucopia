import csv
import pdb
from Car import Car
from CarRegistry import CarRegistry
from tabulate import tabulate


class UI:

    def __init__(self, car_registry):
        self.car_registry = car_registry
        self.exit_flag = False

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
            self.display_menu()
            option = input("Enter your choice: ").upper()

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

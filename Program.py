from Car import Car
from CarRegistry import CarRegistry
from UI import UI
import pdb
from tabulate import tabulate


class Program:
    def main(self):
        car_registry = CarRegistry()

        ui = UI(car_registry)

        while not ui.exit_flag:
            ui.sanitize_data()
            ui.set_cars_data_state()
            ui.display_pretty_table()
            ui.display_menu()
            ui.process_options()
            ui.save_registry_to_file()

            if ui.exit_flag or ui.confirm_exit():
                print('See you soon')
                break


if __name__ == "__main__":
    program = Program()
    program.main()

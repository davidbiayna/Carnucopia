import unittest
from CarRegistry import CarRegistry


class TestCarRegistry(unittest.TestCase):
    def test_set_cars_data(self):
        # Create a CarRegistry instance
        car_registry = CarRegistry()

        # Set the file headers and position values
        car_registry.set_file_headers_and_pos_values()

        # Load data from the CSV file
        car_registry.initial_file_rows = []
        with open("CarRegistry.dat", "r") as file:
            for line in file:
                car_registry.initial_file_rows.append(line.strip().split(','))

        # Set the cars data
        car_registry.set_cars_data()

        # Perform assertions based on the data
        self.assertEqual(len(car_registry.cars), 15)

        car1 = car_registry.cars["car_1"]
        self.assertEqual(car1.registration_plate, "BD61 SLU")
        self.assertEqual(car1.manufacturer, "HONDA")
        self.assertEqual(car1.model_type, "CR-V")
        self.assertEqual(car1.sipp, "SFDR")
        self.assertEqual(car1.seat_capacity, 5)
        self.assertEqual(car1.width, 1780)
        self.assertEqual(car1.length, 4510)
        self.assertEqual(car1.maximum_speed, 130.0)
        self.assertEqual(car1.mpg, 39.0)
        self.assertTrue(car1.on_hire)

        car2 = car_registry.cars["car_2"]
        self.assertEqual(car2.registration_plate, "CA51 MBE")
        self.assertEqual(car2.manufacturer, "CHEVROLET")
        self.assertEqual(car2.model_type, "CORVETTE")
        self.assertEqual(car2.sipp, "JTAV")
        self.assertEqual(car2.seat_capacity, 2)
        self.assertEqual(car2.width, 1877)
        self.assertEqual(car2.length, 1234)
        self.assertEqual(car2.maximum_speed, 194.0)
        self.assertEqual(car2.mpg, 24.0)
        self.assertTrue(car2.on_hire)


if __name__ == '__main__':
    unittest.main()

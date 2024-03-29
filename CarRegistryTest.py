import csv
import pdb
import unittest
from unittest.mock import patch
import io
from CarRegistry import CarRegistry
from Car import Car


class TestCarRegistry(unittest.TestCase):
    def test_init(self):
        registry = CarRegistry()
        self.assertEqual(registry._cars, {})
        self.assertIs(registry._car, Car)
        self.assertEqual(registry.initial_file_rows, [])
        self.assertEqual(registry._prettyfied_cars, {})

        expected_car_attrs = {'Pos': 'pos_id', 'ID': 'car_id', 'Reg': 'registration_plate',
                              "Manufacturer": 'manufacturer',
                              "Model": 'model_type', "SIPP": 'sipp', "Seat": 'seat_capacity',
                              "Width": 'width', "Length": 'length', "Spd": 'maximum_speed',
                              "MPG": 'mpg', "OnHire": 'on_hire'}

        self.assertDictEqual(registry._car_attrs, expected_car_attrs)

    def setUp(self):
        self.instance = CarRegistry()

    def test_add_car(self):
        user_input = ['DB80 DBN', 'AUDI', 'R8', 'JTAV', '2', '1500', '2000', '300', '130', 'F']
        user_input2 = ['DB80 CMF', 'BMW', 'T1', 'JTAV', '2', '1700', '2300', '350', '130', 'T']
        # Creation of two different cars for the purpose of testing

        with unittest.mock.patch('builtins.input', side_effect=user_input):
            self.instance.add_car()

        self.assertIn('car_1', self.instance._cars)
        self.assertEqual(self.instance._cars['car_1'].registration_plate, 'DB80 DBN')
        self.assertEqual(self.instance._cars['car_1'].manufacturer, 'AUDI')
        self.assertEqual(self.instance._cars['car_1'].model_type, 'R8')
        self.assertEqual(self.instance._cars['car_1'].sipp, 'JTAV')
        self.assertEqual(self.instance._cars['car_1'].seat_capacity, 2)
        self.assertEqual(self.instance._cars['car_1'].width, 1500)
        self.assertEqual(self.instance._cars['car_1'].length, 2000)
        self.assertEqual(self.instance._cars['car_1'].maximum_speed, 300)
        self.assertEqual(self.instance._cars['car_1'].mpg, 130)
        self.assertEqual(self.instance._cars['car_1'].on_hire, False)

        with unittest.mock.patch('builtins.input', side_effect=user_input2):
            self.instance.add_car()

        self.assertIn('car_2', self.instance._cars)
        self.assertEqual(self.instance._cars['car_2'].registration_plate, 'DB80 CMF')
        self.assertEqual(self.instance._cars['car_2'].manufacturer, 'BMW')
        self.assertEqual(self.instance._cars['car_2'].model_type, 'T1')
        self.assertEqual(self.instance._cars['car_2'].sipp, 'JTAV')
        self.assertEqual(self.instance._cars['car_2'].seat_capacity, 2)
        self.assertEqual(self.instance._cars['car_2'].width, 1700)
        self.assertEqual(self.instance._cars['car_2'].length, 2300)
        self.assertEqual(self.instance._cars['car_2'].maximum_speed, 350)
        self.assertEqual(self.instance._cars['car_2'].mpg, 130)
        self.assertEqual(self.instance._cars['car_2'].on_hire, True)

    def test_remove_car(self):
        user_input1 = ['DB80 DBN', 'AUDI', 'R8', 'JTAV', '2', '1500', '2000', '300', '130', 'F']
        user_input2 = ['DB80 CMF', 'BMW', 'T1', 'JTAV', '2', '1700', '2300', '350', '130', 'T']
        with unittest.mock.patch('builtins.input', side_effect=user_input1):
            self.instance.add_car()
        with unittest.mock.patch('builtins.input', side_effect=user_input2):
            self.instance.add_car()

        self.assertIn('car_1', self.instance._cars)
        self.assertIn('car_2', self.instance._cars)
        user_input_remove = ['1', 'Y']
        with unittest.mock.patch('builtins.input', side_effect=user_input_remove):
            self.instance.remove_car()

        self.assertNotIn('car_1', self.instance._cars)
        # Deliberately created a second car to assert the deletion of car_1 and car_2 remains intact in car registry
        self.assertIn('car_2', self.instance._cars)

    @patch('builtins.input',
           side_effect=['DB80 DBN', 'AUDI', 'R8', 'JTAV', '2', '1500', '2000', '300', '130', 'F', '1', 'Y'])
    def test_already_returned_car_to_garage(self, mock_input):
        self.instance.add_car()
        self.instance.return_car_to_garage()
        self.assertFalse(self.instance._cars['car_1'].on_hire)
        self.assertTrue('car_1' in self.instance._cars)
        self.assertEqual(self.instance._cars['car_1'].registration_plate, 'DB80 DBN')
        self.assertEqual(self.instance._cars['car_1'].manufacturer, 'AUDI')
        self.assertEqual(self.instance._cars['car_1'].model_type, 'R8')
        self.assertEqual(self.instance._cars['car_1'].sipp, 'JTAV')
        self.assertEqual(self.instance._cars['car_1'].seat_capacity, 2)
        self.assertEqual(self.instance._cars['car_1'].width, 1500)
        self.assertEqual(self.instance._cars['car_1'].length, 2000)
        self.assertEqual(self.instance._cars['car_1'].maximum_speed, 300)
        self.assertEqual(self.instance._cars['car_1'].mpg, 130)
        self.assertEqual(self.instance._cars['car_1'].on_hire, False)

    @patch('builtins.input',
           side_effect=['DB80 DBN', 'AUDI', 'R8', 'JTAV', '2', '1500', '2000', '300', '130', 'T', '1', 'Y'])
    def test_return_car_to_garage_success(self, mock_input):
        self.instance.add_car()
        self.instance.return_car_to_garage()

        self.assertFalse(self.instance._cars['car_1'].on_hire)
        self.assertTrue('car_1' in self.instance._cars)
        self.assertEqual(self.instance._cars['car_1'].registration_plate, 'DB80 DBN')
        self.assertEqual(self.instance._cars['car_1'].manufacturer, 'AUDI')
        self.assertEqual(self.instance._cars['car_1'].model_type, 'R8')
        self.assertEqual(self.instance._cars['car_1'].sipp, 'JTAV')
        self.assertEqual(self.instance._cars['car_1'].seat_capacity, 2)
        self.assertEqual(self.instance._cars['car_1'].width, 1500)
        self.assertEqual(self.instance._cars['car_1'].length, 2000)
        self.assertEqual(self.instance._cars['car_1'].maximum_speed, 300)
        self.assertEqual(self.instance._cars['car_1'].mpg, 130)
        self.assertEqual(self.instance._cars['car_1'].on_hire, False)

    @patch('builtins.input',
           side_effect=['DB80 DBN', 'AUDI', 'R8', 'JTAV', '2', '1500', '2000', '300', '130', 'F', '1', 'N'])
    def test_hire_out_cancel(self, mock_input):
        self.instance.add_car()
        self.instance.hire_out()
        self.assertFalse(self.instance._cars['car_1'].on_hire)

    def test_hire_out_confirm(self):
        user_input1 = ['DB80 DBN', 'AUDI', 'R8', 'JTAV', '2', '1500', '2000', '300', '130', 'F']
        with unittest.mock.patch('builtins.input', side_effect=user_input1):
            self.instance.add_car()

        self.assertIn('car_1', self.instance._cars)
        user_input_hire_out = ['1', 'Y']
        with unittest.mock.patch('builtins.input', side_effect=user_input_hire_out):
            self.instance.hire_out()
        self.assertTrue(self.instance._cars['car_1'].on_hire)


if __name__ == '__main__':
    unittest.main()

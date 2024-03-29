import pdb
import unittest
from UI import UI
from CarRegistry import CarRegistry
import io
import sys


class TestUI(unittest.TestCase):
    def test_init(self):
        ui_instance = UI(car_registry="car_registry")
        self.car_registry = CarRegistry()

        self.assertEqual(ui_instance.car_registry, "car_registry")
        self.assertFalse(ui_instance.exit_flag)

    def setUp(self):
        car_registry_instance = CarRegistry()
        self.ui_instance = UI(car_registry=car_registry_instance)

    def test_display_table_with_headers_pos_values_and_data(self):
        self.ui_instance.sanitize_data()
        self.ui_instance.car_registry.set_cars_data()
        self.ui_instance.display_pretty_table()
        data = self.ui_instance.car_registry._prettyfied_cars
        expected_car_data = [
            {'car_1': {'Pos': 1, 'ID': 1, 'Reg': 'BD61 SLU', 'Manufacturer': 'HONDA', 'Model': 'CR-V', 'SIPP': 'SFDR',
                       'Seat': '5', 'Width': 1780, 'Length': 4510, 'Spd': 130.0, 'MPG': 39.0, 'OnHire': True},
             'car_2': {'Pos': 2, 'ID': 2, 'Reg': 'CA51 MBE', 'Manufacturer': 'CHEVROLET', 'Model': 'CORVETTE',
                       'SIPP': 'JTAV', 'Seat': '2', 'Width': 1877, 'Length': 1234, 'Spd': 194.0, 'MPG': 24.0,
                       'OnHire': True},
             'car_3': {'Pos': 3, 'ID': 3, 'Reg': 'PC14 RSN', 'Manufacturer': 'FORD', 'Model': 'F-150', 'SIPP': 'PQBD',
                       'Seat': '5', 'Width': 2121, 'Length': 5890, 'Spd': 155.0, 'MPG': 20.0, 'OnHire': True},
             'car_4': {'Pos': 4, 'ID': 4, 'Reg': 'MB19 ORE', 'Manufacturer': 'HONDA', 'Model': 'ACCORD', 'SIPP': 'FDAR',
                       'Seat': '5', 'Width': 1849, 'Length': 4933, 'Spd': 125.0, 'MPG': 47.3, 'OnHire': False},
             'car_5': {'Pos': 5, 'ID': 5, 'Reg': 'BD68 NAP', 'Manufacturer': 'HONDA', 'Model': 'ACCORD', 'SIPP': 'FDAV',
                       'Seat': '5', 'Width': 1849, 'Length': 4933, 'Spd': 171.0, 'MPG': 37.7, 'OnHire': False},
             'car_6': {'Pos': 6, 'ID': 6, 'Reg': 'LY51 BED', 'Manufacturer': 'ISUZU', 'Model': 'NQR', 'SIPP': 'OKAD',
                       'Seat': '3', 'Width': 2065, 'Length': 5220, 'Spd': 114.0, 'MPG': 11.9, 'OnHire': True},
             'car_7': {'Pos': 7, 'ID': 7, 'Reg': 'LJ08 NOD', 'Manufacturer': 'HONDA', 'Model': 'CIVIC', 'SIPP': 'SDAR',
                       'Seat': '5', 'Width': 1877, 'Length': 4648, 'Spd': 125.0, 'MPG': 31.0, 'OnHire': True},
             'car_8': {'Pos': 8, 'ID': 9, 'Reg': 'GK63 SLE', 'Manufacturer': 'FORD', 'Model': 'ESCAPE', 'SIPP': 'SDMR',
                       'Seat': '5', 'Width': 1806, 'Length': 4457, 'Spd': 209.0, 'MPG': 23.0, 'OnHire': True},
             'car_9': {'Pos': 9, 'ID': 10, 'Reg': 'GW66 EPY', 'Manufacturer': 'FORD', 'Model': 'TAURUS', 'SIPP': 'FCAR',
                       'Seat': '5', 'Width': 1935, 'Length': 5154, 'Spd': 143.0, 'MPG': 20.0, 'OnHire': False},
             'car_10': {'Pos': 10, 'ID': 11, 'Reg': 'YE02 FOU', 'Manufacturer': 'TOYOTA', 'Model': 'CELICA',
                        'SIPP': 'IDAR', 'Seat': '5', 'Width': 1778, 'Length': 2700, 'Spd': 140.0, 'MPG': 30.0,
                        'OnHire': False},
             'car_11': {'Pos': 11, 'ID': 12, 'Reg': 'YN65 RTY', 'Manufacturer': 'CHRYSLER', 'Model': 'CHEROKEE',
                        'SIPP': 'PFBD', 'Seat': '5', 'Width': 1900, 'Length': 4730, 'Spd': 125.5, 'MPG': 36.0,
                        'OnHire': True},
             'car_12': {'Pos': 12, 'ID': 13, 'Reg': 'WP64 WIN', 'Manufacturer': 'CHEVROLET', 'Model': 'SPARK',
                        'SIPP': 'ECMR', 'Seat': '5', 'Width': 1495, 'Length': 3495, 'Spd': 89.0, 'MPG': 33.0,
                        'OnHire': False},
             'car_13': {'Pos': 13, 'ID': 14, 'Reg': 'RG69 KSD', 'Manufacturer': 'CHEVROLET', 'Model': 'CORVETTE',
                        'SIPP': 'JTAV', 'Seat': '2', 'Width': 1877, 'Length': 1234, 'Spd': 194.0, 'MPG': 24.0,
                        'OnHire': True},
             'car_14': {'Pos': 14, 'ID': 15, 'Reg': 'HR11 OZE', 'Manufacturer': 'FORD', 'Model': 'F-150',
                        'SIPP': 'PPBD', 'Seat': '5', 'Width': 2121, 'Length': 5890, 'Spd': 155.0, 'MPG': 20.0,
                        'OnHire': False}}]
        self.assertDictEqual(data, expected_car_data[0])


if __name__ == '__main__':
    unittest.main()

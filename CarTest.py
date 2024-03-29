import unittest
from Car import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car(1, 1, "AB80 XYZ", "HONDA", "CIVIC", "IDAR", 4, 1500, 4500, 120, 30, True)

    def test_init(self):
        # Arrange
        pos_id = 1
        car_id = 1
        registration_plate = "AB80 XYZ"
        manufacturer = "HONDA"
        model_type = "CIVIC"
        sipp = "IDAR"
        seat_capacity = 4
        width = 1500
        length = 4500
        maximum_speed = 120
        mpg = 30
        on_hire = True

        # Act
        car = Car(pos_id, car_id, registration_plate, manufacturer, model_type, sipp,
                  seat_capacity, width, length, maximum_speed, mpg, on_hire)

        # Assert
        self.assertEqual(car.pos_id, pos_id)
        self.assertEqual(car.car_id, car_id)
        self.assertEqual(car.registration_plate, registration_plate)
        self.assertEqual(car.manufacturer, manufacturer)
        self.assertEqual(car.model_type, model_type)
        self.assertEqual(car.sipp, sipp)
        self.assertEqual(car.seat_capacity, seat_capacity)
        self.assertEqual(car.width, width)
        self.assertEqual(car.length, length)
        self.assertEqual(car.maximum_speed, maximum_speed)
        self.assertEqual(car.mpg, mpg)
        self.assertEqual(car.on_hire, on_hire)

    def test_valid_eq_method(self):
        # Arrange
        first_car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=1780,
            length=4510,
            maximum_speed=130.0,
            mpg=39.0,
            on_hire=True
        )
        # Act
        # assertion
        self.assertTrue(first_car == first_car)

        second_car = Car(
            pos_id=2,
            car_id=2,
            registration_plate="CA51 MBE",
            manufacturer="CHEVROLET",
            model_type="CORVETTE",
            sipp="JTAV",
            seat_capacity=2,
            width=1877,
            length=1234,
            maximum_speed=194.0,
            mpg=24.0,
            on_hire=True
        )

        self.assertFalse(first_car == second_car)

    def test_car_id(self):
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=1780,
            length=4510,
            maximum_speed=130.0,
            mpg=39.0,
            on_hire=True
        )
        self.assertEqual(car.car_id, 1)

    def test_valid_registration_plate_method(self):
        # Arrange
        expected_registration_plate = "BD61 SLU"
        # Act
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate=expected_registration_plate,
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=1780,
            length=4510,
            maximum_speed=130.0,
            mpg=39.0,
            on_hire=True
        )
        # Assert
        self.assertEqual(car.registration_plate, expected_registration_plate)

    def test_invalid_registration_plate_method(self):
        # Arrange
        expected_registration_plate = "BD61 SLU"
        incorrect_registration_plate = "ABC123"

        # Act
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate=incorrect_registration_plate,
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=1780,
            length=4510,
            maximum_speed=130,
            mpg=39,
            on_hire=True
        )
        # Assert
        self.assertNotEqual(car.registration_plate, expected_registration_plate)

    def test_valid_manufacturer_method(self):
        # Arrange
        expected_manufacturer = "HONDA"
        # Act
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer=expected_manufacturer,
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=1780,
            length=4510,
            maximum_speed=130.0,
            mpg=39.0,
            on_hire=True
        )
        # Assert
        self.assertEqual(car.manufacturer, expected_manufacturer)

    def test_invalid_manufacturer_method(self):
        # Arrange
        expected_manufacturer = "HONDA"
        incorrect_manufacturer = "TOYOTA"
        # Act
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer=incorrect_manufacturer,
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=1780,
            length=4510,
            maximum_speed=130,
            mpg=39,
            on_hire=True
        )
        # Assert
        self.assertNotEqual(car.manufacturer, expected_manufacturer)

    def test_valid_model_type(self):
        # Arrange
        expected_model_type = "SUV"
        # Act
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type=expected_model_type,
            sipp="SFDR",
            seat_capacity=5,
            width=1780,
            length=4510,
            maximum_speed=130,
            mpg=39,
            on_hire=True
        )
        # Assert
        self.assertEqual(car.model_type, expected_model_type)

    def test_invalid_model_type(self):
        # Arrange
        expected_model_type = "SUV"
        incorrect_model_type = "SEDAN"
        # Act
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer=incorrect_model_type,
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=1780,
            length=4510,
            maximum_speed=130,
            mpg=39,
            on_hire=True
        )
        # Assert
        self.assertNotEqual(car.model_type, expected_model_type)

    def test_valid_sipp(self):
        # Arrange
        expected_sipp = "SFDR"
        # Act
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp=expected_sipp,
            seat_capacity=5,
            width=1780,
            length=4510,
            maximum_speed=130,
            mpg=39,
            on_hire=True
        )
        # Assert
        self.assertEqual(car.sipp, expected_sipp)

    def test_invalid_sipp(self):
        # Arrange
        expected_sipp = "SFDR"
        incorrect_sipp = "ABCD"
        # Act
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp=incorrect_sipp,
            seat_capacity=5,
            width=1780,
            length=4510,
            maximum_speed=130.0,
            mpg=39.0,
            on_hire=True
        )
        # Assert
        self.assertNotEqual(car.sipp, expected_sipp)

    def test_valid_seat_capacity(self):
        # Arrange
        expected_seat_capacity = 5
        # Act
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=expected_seat_capacity,
            width=1780,
            length=4510,
            maximum_speed=130,
            mpg=39,
            on_hire=True
        )
        # Assert
        self.assertEqual(car.seat_capacity, expected_seat_capacity)

    def test_invalid_seat_capacity(self):
        # Arrange
        expected_seat_capacity = 5
        incorrect_seat_capacity = 12
        # Act
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=incorrect_seat_capacity,
            width=1780,
            length=4510,
            maximum_speed=130.0,
            mpg=39.0,
            on_hire=True
        )
        # Assert
        self.assertNotEqual(car.seat_capacity, expected_seat_capacity)

    def test_valid_width(self):
        # Arrange
        expected_width = 1780
        # Act
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=expected_width,
            length=4510,
            maximum_speed=130,
            mpg=39,
            on_hire=True
        )
        # Assert
        self.assertEqual(car.width, expected_width)

    def test_invalid_width(self):
        # Arrange
        expected_width = 1780
        incorrect_width = 3000
        # Act
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=incorrect_width,
            length=4510,
            maximum_speed=130,
            mpg=39,
            on_hire=True
        )
        # Assert
        self.assertNotEqual(car.width, expected_width)

    def test_valid_length(self):
        # Arrange
        expected_length = 4510
        # Act
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=1780,
            length=expected_length,
            maximum_speed=130,
            mpg=39,
            on_hire=True
        )
        # Assert
        self.assertEqual(car.length, expected_length)

    def test_invalid_length(self):
        # Arrange
        expected_length = 4510
        incorrect_length = 12000
        # Act
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=1780,
            length=incorrect_length,
            maximum_speed=130,
            mpg=39,
            on_hire=True
        )
        # Assert
        self.assertNotEqual(car.length, expected_length)

    def test_maximum_speed(self):
        # Arrange
        expected_maximum_speed = 130
        # Act
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=1780,
            length=4510,
            maximum_speed=expected_maximum_speed,
            mpg=39,
            on_hire=True
        )
        # Assert
        self.assertEqual(car.maximum_speed, expected_maximum_speed)

    def test_invalid_maximum_speed(self):
        # Arrange
        expected_maximum_speed = 130
        incorrect_maximum_speed = -1
        # Act
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=1780,
            length=4510,
            maximum_speed=incorrect_maximum_speed,
            mpg=39,
            on_hire=True
        )
        # Assert
        self.assertNotEqual(car.maximum_speed, expected_maximum_speed)

    def test_valid_mpg(self):
        # Arrange
        expected_mpg = 39
        # Act
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=1780,
            length=4510,
            maximum_speed=130,
            mpg=expected_mpg,
            on_hire=True
        )
        # Assert
        self.assertEqual(car.mpg, expected_mpg)

    def test_invalid_mpg(self):
        # Arrange
        expected_mpg = 39
        incorrect_mpg = -1
        # Act
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=1780,
            length=4510,
            maximum_speed=130.,
            mpg=incorrect_mpg,
            on_hire=True
        )
        # Assert
        self.assertNotEqual(car.mpg, expected_mpg)

    def test_valid_on_hire(self):
        # Arrange
        expected_on_hire = True
        # Act
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=1780,
            length=4510,
            maximum_speed=130,
            mpg=39,
            on_hire=expected_on_hire
        )
        # Assert
        self.assertEqual(car.on_hire, expected_on_hire)

    def test_invalid_on_hire(self):
        # Arrange
        expected_on_hire = False
        incorrect_on_hire = 123
        # Act
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=1780,
            length=4510,
            maximum_speed=130,
            mpg=39,
            on_hire=incorrect_on_hire
        )
        # Assert
        self.assertEqual(car.on_hire, expected_on_hire)

    def test_is_valid_with_missing_attributes(self):
        # Arrange
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=1780,
            length=4510,
            maximum_speed=130,
            mpg=39,
            on_hire=True
        )
        # Act
        car.seat_capacity = -1
        # Assert
        self.assertFalse(car.is_valid(car))

    def test_is_valid_with_all_attributes(self):
        # Arrange
        car = Car(
            pos_id=1,
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=1780,
            length=4510,
            maximum_speed=130,
            mpg=39,
            on_hire=True
        )

        # Act & Assert
        self.assertTrue(car.is_valid(car))


if __name__ == '__main__':
    unittest.main()

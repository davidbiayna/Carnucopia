from Car import Car
import unittest


class MyTestCase(unittest.TestCase):
    def test_valid_init_method(self):
        # Arrange
        # Act
        first_car = Car(
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

        # Assertion
        self.assertEqual(1, first_car.car_id)
        self.assertEqual("BD61 SLU", first_car.registration_plate)
        self.assertEqual("HONDA", first_car.manufacturer)
        self.assertEqual("CR-V", first_car.model_type)
        self.assertEqual("SFDR",first_car.sipp)
        self.assertEqual(5, first_car.seat_capacity)
        self.assertEqual(1780, first_car.width)
        self.assertEqual(4510, first_car.length)
        self.assertEqual(130.0, first_car.maximum_speed)
        self.assertEqual(39.0, first_car.mpg)
        self.assertEqual(True, first_car.on_hire)

    def test_valid_eq_method(self):
        # Arrange
        # Act
        first_car = Car(
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
        # assertion
        self.assertTrue(first_car == first_car)

        second_car = Car(
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

    def test_valid_registration_plate_method(self):
        # Arrange
        valid_registration_plate = "BD61 SLU"
        # Act
        car = Car(
            car_id=1,
            registration_plate=valid_registration_plate,
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

        self.assertEqual(car.registration_plate, valid_registration_plate)

    def test_invalid_registration_plate_method(self):
        # Arrange
        invalid_registration_plate = "Invalid Plate"
        # Act
        car = Car(
            car_id=1,
            registration_plate=invalid_registration_plate,
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
        self.assertEqual(car.registration_plate, "DEFAULT")

    def test_valid_sipp_method(self):
        # Arrange
        valid_sipp = "SFDR"
        # Act
        car = Car(
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp=valid_sipp,
            seat_capacity=5,
            width=1780,
            length=4510,
            maximum_speed=130.0,
            mpg=39.0,
            on_hire=True
        )
        self.assertEqual(car.sipp, valid_sipp)

    def test_invalid_sipp_method(self):
        # Arrange
        invalid_sipp = "Invalid SIPP"
        # Act
        car = Car(
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp=invalid_sipp,
            seat_capacity=5,
            width=1780,
            length=4510,
            maximum_speed=130.0,
            mpg=39.0,
            on_hire=True
        )
        self.assertEqual(car.sipp, "DEFAULT")

    def test_valid_seat_capacity(self):
        # Arrange
        valid_seat_capacity = 5
        # Act
        car = Car(
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=valid_seat_capacity,
            width=1780,
            length=4510,
            maximum_speed=130.0,
            mpg=39.0,
            on_hire=True
        )
        self.assertEqual(car.seat_capacity, valid_seat_capacity)

    def test_invalid_seat_capacity(self):
        # Arrange
        invalid_seat_capacity = 10
        # Act
        car = Car(
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=invalid_seat_capacity,
            width=1780,
            length=4510,
            maximum_speed=130.0,
            mpg=39.0,
            on_hire=True
        )
        self.assertEqual(car.seat_capacity, None)

    def test_valid_width(self):
        # Arrange
        valid_width = 1500
        # Act
        car = Car(
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=valid_width,
            length=4510,
            maximum_speed=130.0,
            mpg=39.0,
            on_hire=True
        )
        self.assertEqual(car.width, valid_width)

    def test_invalid_width(self):
        # Arrange
        invalid_width = 3000
        # Act
        car = Car(
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=invalid_width,
            length=4510,
            maximum_speed=130.0,
            mpg=39.0,
            on_hire=True
        )
        self.assertEqual(car.width, 0)

    def test_valid_length(self):
        # Arrange
        valid_length = 2000
        # Act
        car = Car(
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=1780,
            length=valid_length,
            maximum_speed=130.0,
            mpg=39.0,
            on_hire=True
        )
        self.assertEqual(car.length, valid_length)

    def test_invalid_length(self):
        # Arrange
        invalid_length = 15000
        # Act
        car = Car(
            car_id=1,
            registration_plate="BD61 SLU",
            manufacturer="HONDA",
            model_type="CR-V",
            sipp="SFDR",
            seat_capacity=5,
            width=1780,
            length=invalid_length,
            maximum_speed=130.0,
            mpg=39.0,
            on_hire=True
        )
        self.assertEqual(car.length, 0)


if __name__ == '__main__':
    unittest.main()

from Car import Car
from CarRegistry import CarRegistry
import unittest


class MyTestCase(unittest.TestCase):

    def test_init_method(self):
        # Arrange
        registry = CarRegistry()

        # Assert
        self.assertIsNone(registry._hire_out, "hire_out should be initialized to None.")
        self.assertEqual(len(registry._cars), 0, "The _cars list should be empty.")

    def test_add_car_method(self):
        # Arrange
        registry = CarRegistry()
        car = Car(
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
        registry.add_car(car)

        # Assert
        self.assertIn(car, registry.get_cars())

    def test_remove_car_method(self):
        # Arrange
        registry = CarRegistry()
        car = Car(
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
        registry.remove_car(car)

        # Assert
        self.assertNotIn(car, registry.get_cars())
        print(f"car {car.registration_plate} has been removed from registry")

    def test_return_car_to_garage_successful_return(self):
        # Arrange
        registry = CarRegistry()
        car = Car(
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
        registry.add_car(car)
        result = registry.return_car_to_garage(1)

        # Assert
        self.assertEqual(result, f"The car registered as {car.registration_plate} has successfully returned to the "
                                 f"garage")
        self.assertFalse(car.on_hire)

    def test_return_car_to_garage_already_in_garage(self):
        # Arrange
        registry = CarRegistry()
        car = Car(
            car_id=4,
            registration_plate="MB19 ORE",
            manufacturer="HONDA",
            model_type="ACCORD",
            sipp="FDAR",
            seat_capacity=5,
            width=1849,
            length=4933,
            maximum_speed=125.0,
            mpg=47.3,
            on_hire=False  # The car is not on hire initially (in the garage)
        )

        # Act
        registry.add_car(car)
        result = registry.return_car_to_garage(4)

        # Assert
        expected_message = f"Sorry, the car registered as {car.registration_plate} is already in the garage"
        self.assertEqual(result, expected_message)
        print(expected_message)
        self.assertFalse(car.on_hire, "The car should not be on hire after returning to the garage")


if __name__ == '__main__':
    unittest.main()

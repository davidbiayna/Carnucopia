import re
import pdb

from tabulate import tabulate


class Car:
    minimum_width = 1000
    maximum_width = 2500
    minimum_length = 1000
    maximum_length = 10000
    _largest_car_id = 0

    manufacturers = ["CHEVROLET",
                     "CHRYSLER",
                     "FORD",
                     "HONDA",
                     "ISUZU",
                     "TOYOTA",
                     "AUDI",
                     "BMW",
                     "MERCEDES",
                     "VOLKSWAGEN",
                     "SUBARU",
                     "NISSAN",
                     "MAZDA",
                     "LEXUS",
                     "JEEP",
                     "HYUNDAI",
                     "KIA",
                     "PEUGEOT"
                     "FIAT"
                     "VOLVO"]

    def __init__(self, pos_id, car_id, registration_plate, manufacturer, model_type, sipp,
                 seat_capacity, width, length, maximum_speed, mpg, on_hire):
        self.pos_id = int(pos_id)
        self.car_id = int(car_id)
        self.registration_plate = registration_plate
        self.manufacturer = manufacturer
        self.model_type = model_type
        self.sipp = sipp
        self.seat_capacity = seat_capacity
        self.width = int(width)
        self.length = int(length)
        self.maximum_speed = float(maximum_speed)
        self.mpg = float(mpg)
        self.on_hire = on_hire

    def __eq__(self, other):
        return isinstance(other, Car) and self.registration_plate == other.registration_plate

    @property
    def car_id(self):
        return self._car_id

    @car_id.setter
    def car_id(self, value):
        self._car_id = value

    @property
    def registration_plate(self):
        return self._registration_plate

    @registration_plate.setter
    def registration_plate(self, value):
        registration_plate_format = (r"(^[A-Z]{2}[0-9]{2}\s?[A-Z]{3}$)|(^[A-Z][0-9]{1,3}[A-Z]{3}$)|(^[A-Z]{3}[0-9]{1,"
                                     r"3}[A-Z]$)|(^[0-9]{1,4}[A-Z]{1,2}$)|(^[0-9]{1,3}[A-Z]{1,3}$)|(^[A-Z]{1,2}[0-9]{1,"
                                     r"4}$)|(^[A-Z]{1,3}[0-9]{1,3}$)|(^[A-Z]{1,3}[0-9]{1,4}$)|(^[0-9]{3}[DX]{1}[0-9]{"
                                     r"3}$)")
        try:
            if re.match(registration_plate_format, value):
                self._registration_plate = value
            else:
                raise ValueError("Invalid UK registration plate format")
        except ValueError as e:
            print(e)
            self._registration_plate = None

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        try:
            if value.upper() in self.manufacturers:
                self._manufacturer = value.upper()
            else:
                raise ValueError("Invalid manufacturer,setting back to default")
        except ValueError as e:
            print(e)
            self._manufacturer = None

    @property
    def model_type(self):
        return self._model_type

    @model_type.setter
    def model_type(self, value):
        self._model_type = value

    @property
    def sipp(self):
        return self._sipp

    @sipp.setter
    def sipp(self, value):
        sipp_format = r"(^[CDEFGHIJOPRSU][BCDFKLPQTVW][ABCDNM][CDEHINQRVZ]$)"
        try:
            if re.match(sipp_format, value):
                self._sipp = value
            else:
                raise ValueError(f"Invalid SIPP Code {value}, please check again")
        except ValueError as e:
            print(e)
            self._sipp = None

    @property
    def seat_capacity(self):
        return self._seat_capacity

    @seat_capacity.setter
    def seat_capacity(self, value):
        try:
            if 1 <= int(value) <= 10:
                self._seat_capacity = value
            else:
                raise ValueError("Seat capacity out of range (1-10), setting back to default")
        except ValueError as e:
            print(e)
            self._seat_capacity = None

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        try:
            if self.minimum_width <= value <= self.maximum_width:
                self._width = value
            else:
                raise ValueError("Width out of range")
        except ValueError as e:
            print(e)
            self._width = None

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        try:
            if self.minimum_length <= value <= self.maximum_length:
                self._length = value
            else:
                raise ValueError("Length out of range")
        except ValueError as e:
            print(e)
            self._length = None

    @property
    def maximum_speed(self):
        return self._maximum_speed

    @maximum_speed.setter
    def maximum_speed(self, value):
        try:
            if isinstance(value, float) and value >= 0:
                self._maximum_speed = float(value)
            else:
                raise ValueError("Invalid maximum speed,setting back to default")
        except ValueError as e:
            print(e)
            self._maximum_speed = None

    @property
    def mpg(self):
        return self._mpg

    @mpg.setter
    def mpg(self, value):
        try:
            if isinstance(value, float) and value >= 0:
                self._mpg = float(value)
            else:
                raise ValueError("Invalid mpg,setting back to default")
        except ValueError as e:
            print(e)
            self._mpg = None

    @property
    def on_hire(self):
        return self._on_hire

    @on_hire.setter
    def on_hire(self, value):
        try:
            if isinstance(value, str):
                value = value.lower()
                if value == 'true' or value == 't':
                    self._on_hire = True
                else:
                    self._on_hire = False
            elif isinstance(value, bool):
                self._on_hire = value
            else:
                raise ValueError("Invalid on_hire value, setting back to default")
        except ValueError as e:
            print(e)
            self._on_hire = False

    def is_valid(self, car_instance):
        missing_attributes = [key for key, value in self.__dict__.items() if value is None]

        if missing_attributes:
            return False
        else:
            return True

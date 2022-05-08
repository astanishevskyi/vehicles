from abc import ABC, abstractmethod


class Vehicle(ABC):
    total_number = 0

    def __init__(self, nr_wheels, top_speed: int, color: str):
        self.nr_wheels = nr_wheels
        self.color = color
        self.top_speed = top_speed
        self._speed = None

        Vehicle.total_number += 1
        self.count = Vehicle.total_number

    def __str__(self):
        return f"{self.__class__.__name__} " \
               f"- nr_wheels: {self.nr_wheels} " \
               f"- color: {self.color} " \
               f"- top speed: {self.top_speed}"

    def __del__(self):
        Vehicle.total_number -= 1
        del self

    def start_engine(self):
        return range(0, self.top_speed)

    def get_real_max_speed(self) -> int:
        return self.top_speed - self.air_resistance

    @staticmethod
    def convert_to_mph(km_speed) -> float:
        return round(km_speed / 1.6, 1)

    @property
    @abstractmethod
    def air_resistance(self):
        pass


class Motorbike(Vehicle):
    air_resistance = 15


class Truck(Vehicle):
    air_resistance = 50


if __name__ == '__main__':
    m1 = Motorbike(nr_wheels=2, top_speed=170, color='black')
    m2 = Motorbike(nr_wheels=2, top_speed=190, color='red')
    t1 = Truck(nr_wheels=18, top_speed=150, color='white')
    t2 = Truck(nr_wheels=16, top_speed=140, color='blue')

    print('total_number =', Vehicle.total_number)
    del m1
    print('total_number =', Vehicle.total_number)

    m2.speed = 121
    print('m2 speed =', m2.speed)
    m2.speed = 21
    print('m2 speed =', m2.speed)

from abc import ABC, abstractmethod


class SpeedType:
    def __init__(self, top_speed: int):
        self.top_speed = top_speed
        self.speed = None

    def get_real_max_speed(self, air_resistance) -> int:
        return self.top_speed - air_resistance

    @staticmethod
    def convert_to_mph(km_speed) -> float:
        return round(km_speed / 1.6, 1)


class Vehicle(ABC):
    total_number = 0

    def __init__(self, nr_wheels: int, color: str, speed_type: SpeedType):
        self.nr_wheels = nr_wheels
        self.color = color
        self.speed_type = speed_type
        self._speed = None

        Vehicle.total_number += 1
        self.count = Vehicle.total_number

    def __str__(self):
        return f"{self.__class__.__name__} " \
               f"- nr_wheels: {self.nr_wheels} " \
               f"- color: {self.color} " \
               f"- top speed: {self.speed_type.top_speed}"

    def __del__(self):
        Vehicle.total_number -= 1
        del self

    @property
    def speed(self):
        return self.speed_type.speed

    @speed.setter
    def speed(self, value):
        if value > 50:
            self.speed_type.speed = value
        else:
            print("Speed has to be over 50 km/h")

    def start_engine(self):
        return range(0, self.speed.top_speed)

    def get_real_max_speed(self) -> int:
        return self.speed_type.get_real_max_speed(self.air_resistance)

    def convert_to_mph(self, speed) -> float:
        return self.speed_type.convert_to_mph(speed)

    @property
    @abstractmethod
    def air_resistance(self):
        pass


class Motorbike(Vehicle):
    air_resistance = 15


class Truck(Vehicle):
    air_resistance = 50


if __name__ == '__main__':
    sm1 = SpeedType(170)
    sm2 = SpeedType(190)
    st1 = SpeedType(150)
    st2 = SpeedType(140)
    m1 = Motorbike(nr_wheels=2, speed_type=sm1, color='black')
    m2 = Motorbike(nr_wheels=2, speed_type=sm2, color='red')
    t1 = Truck(nr_wheels=18, speed_type=st1, color='white')
    t2 = Truck(nr_wheels=16, speed_type=st2, color='blue')

    print('total_number =', Vehicle.total_number)
    del m1
    print('total_number =', Vehicle.total_number)

    m2.speed = 121
    print('m2 speed =', m2.speed)
    m2.speed = 21
    print('m2 speed =', m2.speed)

class Transport:
    def __init__(self, speed: int, brand: str, year: int, number: int, pos_x: int, pos_y: int):
        self.coordinates = pos_x, pos_y
        self.speed = speed
        self.brand = brand
        self.year = year
        self.number = number


    def __str__(self):
        """
           Представление всей информации для вывода в методе print()
        """
        return ('Coordinates: {}, speed: {}, brand: {}, year: {}, number: {}'
                .format(self.coordinates, self.speed, self.brand, self.year, self.number))


    @property
    def coordinates(self):
        return self.coordinates

    @coordinates.setter
    def coordinates(self, pos_x: int, pos_y: int):
        self.coordinates = pos_x, pos_y

    @property
    def speed(self):
        return self.speed

    @speed.setter
    def speed(self, speed: int):
        if speed >= 0:
            self.speed = speed

    @property
    def brand(self):
        return self.brand

    @brand.setter
    def brand(self, brand: str):
        self.brand = brand

    @property
    def year(self):
        return self.year

    @year.setter
    def year(self, year: int):
        if year > 0 and len(str(year)) == 4:
            self.year = year

    @property
    def number(self):
        return self.number

    @number.setter
    def number(self, number: int):
        if number > 0:
            self.number = number


    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        """
        Присутствие транспортного средства в пределах заданной области
        pos_x, pos_y - координата левого верхнего угла области
        length, width - длина и ширина области
        """
        if (pos_x <= self.coordinates[0] <= pos_x + length) and (pos_y <= self.coordinates[1] <= pos_y + width):
            return True
        else:
            return False


class Passenger:

    def __init__(self, passengers_capacity, number_of_passengers):
        self.passengers_capacity = passengers_capacity
        self.number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self.passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if  isinstance(passengers_capacity, int) and passengers_capacity > 0:
            self.passengers_capacity = passengers_capacity
        else:
            raise Exception("Недопустимая вместимость")

    @property
    def number_of_passengers(self):
        return self.number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if isinstance(number_of_passengers, int) and 0 <= number_of_passengers <= self.passengers_capacity:
            self.passengers_capacity = number_of_passengers
        else:
            raise Exception("Недопустимое число пассажиров")


class Cargo:
    def __init__(self, carrying: str):
        self.carrying = carrying

    @property
    def carrying(self):
        return self.carrying

    @carrying.setter
    def carrying(self, carrying: str):
        self.carrying = carrying


class Plane(Transport):
    def __init__(self, speed: int, brand: str, year: int, number: int, pos_x: int, pos_y: int, height: int):
        super().__init__(speed, brand, year, number, pos_x, pos_y)
        self.height = height

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, height: int):
        if height >= 0:
            self.height = height

class Auto(Transport):
    def __init__(self, engine_is_electric: bool, engine_is_petrol : bool, number_of_wheels: int, speed: int, brand: str, year: int, number: int, pos_x: int, pos_y: int):
        super().__init__(speed, brand, year, number, pos_x, pos_y)
        self.number_of_wheels = number_of_wheels
        self.engine_is_electric = engine_is_electric
        self.engine_is_petrol  = engine_is_petrol
        self.engine_is_mixed = engine_is_electric * engine_is_petrol

    @property
    def number_of_wheels(self):
        return self.number_of_wheels

    @number_of_wheels.setter
    def number_of_wheels(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels

    @property
    def engine_is_electric(self):
        return self.engine_is_electric

    @engine_is_electric.setter
    def engine_is_electric(self, engine_is_electric: bool):
        self.engine_is_electric = engine_is_electric

    @property
    def engine_is_petrol(self):
        return self.engine_is_petrol

    @engine_is_petrol.setter
    def engine_is_petrol(self, engine_is_petrol: bool):
        self.engine_is_petrol = engine_is_petrol

    @property
    def engine_is_mixed(self):
        return self.engine_is_mixed

    @engine_is_mixed.setter
    def engine_is_mixed(self, engine_is_mixed: bool):
        self.engine_is_mixed = engine_is_mixed

class Ship(Transport):
    def __init__(self, name: str, port: str, speed: int, brand: str, year: int, number: int, pos_x: int, pos_y: int):
        super().__init__(speed, brand, year, number, pos_x, pos_y)
        self.name = name
        self.port = port

    @property
    def port(self):
        return self.port

    @port.setter
    def port(self, port: str):
        self.port = port

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name: str):
        self.name = name


class Car(Auto):
class Bus(Auto, Passenger):
class CargoAuto(Auto, Cargo):

class Boat(Ship):
class PassengerShip(Ship, Passenger):
class CargoShip(Ship, Cargo):

class PassengerPlane(Plane, Passenger):
class CargoPlane(Plane, Cargo):
class Seaplane(Plane, Ship):
from typing import List
import math


class Animal:
    def __init__(self, name: str, age: int, is_mammal: bool, is_male: bool):
        self.name = name
        self.age = age
        self.mammal = is_mammal
        self.is_male = is_male


class Location:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_distance(self, other_point):
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        return distance

    def get_location(self):
        return self


class Store(Location):
    def __init__(self, x, y, name: str, employee_count: int):
        Location.__init__(self, x, y)
        self.name = name
        self.employee_count = employee_count

    def __str__(self):
        return self.name


class Restaurant(Store):
    def __init__(self, x: int, y: int, name: str, employee_count: int):
        Store.__init__(self, x, y, name, employee_count)
        self.name = name
        self.employee_count = employee_count


class Exhibit(Location):
    def __init__(self, x: int, y: int, name: str, price_to_enter: float, employee_count: int):
        Location.__init__(self, x, y)
        self.name = name
        self.price_to_enter = price_to_enter
        self.employee_count = employee_count


# Animals

class Giraffe(Animal):
    def __init__(self, name: str, age: int, is_mammal: bool, is_male: bool, neck_in_inches: int):
        Animal.__init__(self, name, age, is_mammal, is_male)
        self.neck_length = neck_in_inches


class Lion(Animal):

    def __init__(self, name: str, age: int, is_mammal: bool, is_male: bool, teeth_count: int):
        Animal.__init__(self, name, age, is_mammal, is_male)
        self.teeth_count = teeth_count


class Spider(Animal):

    def __init__(self, name: str, age: int, is_mammal: bool, is_male: bool, leg_count: int):
        Animal.__init__(self, name, age, is_mammal, is_male)
        self.leg_count = leg_count


# Stores


class SouvenirShop(Store):
    def __init__(self, x: int, y: int, name: str, theme: str, employee_count: int):
        Store.__init__(self, x, y, name, employee_count)
        self.theme = theme


class ClothingStore(Store):
    def __init__(self, x: int, y: int, name: str, employee_count: int, brands_offered: List[str]):
        Store.__init__(self, x, y, name, employee_count)
        self.brands_offered = brands_offered


# Exhibits

class WaterPark(Exhibit):
    def __init__(self, x: int, y: int, name: str, price_to_enter: float, employee_count: int, customer_count: int):
        Exhibit.__init__(self, x, y, name, price_to_enter, employee_count)
        self.customer_count = customer_count


class Zoo:
    def __init__(
            self, name: str, stores: List[Store], animals: List[Animal],
            exhibits: List[Exhibit], restaurants: List[Restaurant]
    ):
        self.name = name
        self.stores = stores
        self.animals = animals
        self.exhibits = exhibits
        self.restaurants = restaurants


if __name__ == "__main__":
    mathew_souvenirs = SouvenirShop(230, 460, "Mathew Souvenirs", "Hats", 7)
    nike = ClothingStore(570, 150, "Nike", 14, ["Nike"])

    stores = [mathew_souvenirs, nike]

    giraffe1 = Giraffe("Jared", 13, True, True, 48)
    lion1 = Lion("Carly", 7, True, False, 42)
    spider1 = Spider("Bob", 3, False, True, 8)

    animals = [giraffe1, lion1, spider1]

    exhibit1 = WaterPark(140, 650, "Mathew's Waterpark", 14.99, 12, 43)

    exhibits = [exhibit1]

    mcdonalds = Restaurant(10, 400, "McDonald's", 10)
    wendys = Restaurant(100, 750, "Wendy's", 8)

    restaurants = [mcdonalds, wendys]

    zoo1 = Zoo("Crazy Zoo", stores, animals, exhibits, restaurants)
    print(zoo1.stores[0])

    print(zoo1.restaurants[0].get_distance(zoo1.restaurants[1].get_location()))

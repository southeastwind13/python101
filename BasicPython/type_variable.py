'''
Generic Type

-- Old --
T = TypeVar('T') for the generic parameter of the function
ClassName(Generic[T]) for declare the generic parameter in the class

-- New --
We can declare all generic class in the []

1. We use [T] after function name before declare the parameter to specify this
is a generic function
def function_name[T](parameter: list[T]) -> T: ...

2. We use [T] after class name before declare the parameter to specify this is 
a generic class.

'''
from dataclasses import dataclass
from typing import TypeVar

type IntOrStr = int | str
type ListOrSet[T] = list[T] | set[T]



class Box[T]:
    def __init__(self, item: T):
        self.item = item

    def get_item(self) -> T:
        return self.item
    
    def set_item(self, new_item: T) -> None:
        self.item = new_item


def get_first_item[T](items: list[T]) -> T:
    return items[0]

my_list = [1, 2, 3]
print(get_first_item(my_list))


'--- Upper bound class'
@dataclass
class Vehicle:
    model:str

class Car(Vehicle):
    def display(self) -> None:
        print(f'Car model: {self.model}')

class Boat(Vehicle):
    def display(self) -> None:
        print(f'Boat model: {self.model}')



class VehicleRegistry[V: Vehicle]:
    def __init__(self) -> None:
        self.vehicles: list[V] = []

    def __getitem__(self):
        return self.vehicles

    def add_vehicle(self, vehicle: V) -> None:
        self.vehicles.append(vehicle)

    def display_all(self) -> None:
        for vehicle in self.vehicles:
            vehicle.display()

class CofferMachine():
    pass


registry = VehicleRegistry[Car]()
registry.add_vehicle(Car("Sedan"))
registry.add_vehicle(Boat("Cruiser")) # Why it isn't error?
registry.add_vehicle(CofferMachine()) #
registry.display_all()
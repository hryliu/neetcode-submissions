class Vehicle(ABC):
    @abstractmethod
    def getType(self) -> str:
        pass

class Car(Vehicle):
    def getType(self) -> str:
        return "Car"

class Bike(Vehicle):
    def getType(self) -> str:
        return "Bike"

class Truck(Vehicle):
    def getType(self) -> str:
        return "Truck"

class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self) -> Vehicle:
        pass

class CarFactory(VehicleFactory):
    def createVehicle(self) -> Car:
        new_car = Car()
        # self.cars.append(new_car)
        return new_car

class BikeFactory(VehicleFactory):
    def createVehicle(self) -> Car:
        new_bike = Bike()
        # self.bikes.append(new_bike)
        return new_bike

class TruckFactory(VehicleFactory):
    def createVehicle(self) -> Car:
        new_truck = Truck()
        return new_truck

class Car:
    def driver(self):
        return "driving a car"

class Bike:
    def driver(self):
        return "riding a bike"

class VehicleFactory:
    @staticmethod

    def get_vehicle(type):
        if type == 'car':
            return Car()
        elif type == 'bike':
            return Bike()
        else:
            return ValueError



v = VehicleFactory.get_vehicle('bike')
print(v.driver())

vc = VehicleFactory.get_vehicle('car')
print(vc.driver())
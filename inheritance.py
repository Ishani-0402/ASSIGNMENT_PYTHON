# Define the base class 'Vehicle'
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")

# Define the derived class 'Car'
class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of Doors: {self.num_doors}")

    def start_engine(self):
        print("Car engine started")

# Define the derived class 'Motorcycle'
class Motorcycle(Vehicle):
    def __init__(self, make, model, is_offroad):
        super().__init__(make, model)
        self.is_offroad = is_offroad

    def display_info(self):
        super().display_info()
        if self.is_offroad:
            print("Off-road Motorcycle")
        else:
            print("Street Motorcycle")

    def kickstart(self):
        print("Motorcycle kickstarted")

# Create instances of the classes
car1 = Car("Toyota", "Camry", 4)
motorcycle1 = Motorcycle("Harley-Davidson", "Sportster", False)

# Display information about the vehicles
print("Car Information:")
car1.display_info()
car1.start_engine()

print("\nMotorcycle Information:")
motorcycle1.display_info()
motorcycle1.kickstart()

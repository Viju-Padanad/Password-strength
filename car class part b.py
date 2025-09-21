class Car:
    def _init_(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Car Details:")
        print(f"Make : {self.make}")
        print(f"Model: {self.model}")
        print(f"Year : {self.year}")


# Taking input
make = input("Enter car make: ")
model = input("Enter car model: ")
year = int(input("Enter car year: "))

# Create object
car1 = Car(make, model, year)

# Display details
car1.display_details()
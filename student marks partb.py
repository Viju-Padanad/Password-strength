class Student:
    def _init_(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def total_marks(self):
        return self.m1 + self.m2 + self.m3

    def average_marks(self):
        return self.total_marks() / 3

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.m1}, {self.m2}, {self.m3}")
        print(f"Total Marks: {self.total_marks()}")
        print(f"Average Marks: {self.average_marks():.2f}")


# Taking input
name = input("Enter student name: ")
m1 = int(input("Enter marks in Subject 1: "))
m2 = int(input("Enter marks in Subject 2: "))
m3 = int(input("Enter marks in Subject 3: "))

# Create object
student = Student(name, m1, m2, m3)

# Display results
student.display()
class Student:
    def __init__(self, name, marks):
        # Public attribute
        self.name = name
        # Protected attribute
        self._marks = marks
        # Private attribute
        self.__roll_no = "123"

    def get_roll_no(self):
        return self.__roll_no
    
    def get_marks(self):
        return self._marks
    
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self._marks = marks
        else:
            print("Invalid marks")


# Demonstrating encapsulation
s1 = Student("Avanish", 55)

# Accessing public attribute
print("Name (public):", s1.name)

# Accessing private attribute through getter
print("Roll No (private):", s1.get_roll_no())

# Accessing protected attribute through getter
print("Marks (protected):", s1.get_marks())

# Using setter to modify marks
s1.set_marks(85)
print("Updated Marks:", s1.get_marks())

# Testing invalid marks
s1.set_marks(150)


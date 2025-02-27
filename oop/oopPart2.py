from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        """
        Abstract method to calculate the area of the shape
        """
        pass

    @abstractmethod
    def parameter(self):
        """
        Abstract method to calculate the parameter of the shape
        """
        pass

    @abstractmethod
    def display_info(self):
        """
        Abstract method to display the information of the shape
        """
        pass

class circle(shape):
    """
    Circle class that inherits from shape class
    """

    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        """
        Method to calculate the area of the circle
        """
        return 3.14 * self.radius * self.radius
        
    def parameter(self):
        """
        Abstract method to calculate the parameter of circle
        """
        return 2 * 3.14 * self.radius
    
    def display_info(self):
        """
        Abstract method to display the information of circle
        """
        print(f"circle with radius {self.radius}")

class rectangle(shape):
    """
    Rectangle class that inherits from shape class
    """

    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        """
        Method to calculate the area of the Rectangle
        """
        return self.length * self.width
        
    def parameter(self):
        """
        Abstract method to calculate the parameter of Rectangle
        """
        return 2 * self.length * self.width
    
    def display_info(self):
        """
        Abstract method to display the information of Rectangle
        """
        print(f"rectangle with length {self.length} and width {self.width}")

#example
circle = circle(5)
rectangle = rectangle(4,6)

shapes = [circle, rectangle]

for shape in shapes:
    print(f"Area: {shape.area()}")
    print(f"Parameter: {shape.parameter()}")
    print(f"Display info: {shape.display_info()}")
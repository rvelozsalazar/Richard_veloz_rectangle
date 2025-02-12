############################################################################
##Client code to test the Rectangle and Point classes
## Name: Richard Veloz Salazar 
## Class: DEV 128   
## Date: February 8th, 2025
## 
############################################################################

class Point:
    """Represents a point in a 2D space."""
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def translate(self, dx, dy):
        """Moves the point by dx and dy."""
        self.__x += dx
        self.__y += dy


class Rectangle:
    """Represents a rectangle with a top-left point, width, and height."""
    
    # Static Attributes
    DEFAULT_WIDTH = 1
    DEFAULT_HEIGHT = 1
    rectangleCount = 0

    def __init__(self, topLeft, width, height):
        if width <= 0:
            print('Width cannot be negative or zero. Setting it to the default value of 1.')
            width = self.DEFAULT_WIDTH
        if height <= 0:
            print('Height cannot be negative or zero. Setting it to the default value of 1.')
            height = self.DEFAULT_HEIGHT
        
        self.__topLeft = topLeft
        self.__width = width
        self.__height = height

        # Increment count of rectangles created
        Rectangle.rectangleCount += 1

    @property
    def topLeft(self):
        """Returns the top-left corner point of the rectangle."""
        return self.__topLeft

    @topLeft.setter
    def topLeft(self, new_topLeft):
        """Updates the top-left corner of the rectangle."""
        self.__topLeft = new_topLeft

    @property
    def width(self):
        """Returns the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width, ensuring it's greater than zero."""
        if value > 0:
            self.__width = value
        else:
            print('Invalid width. Width must be greater than zero.')

    @property
    def height(self):
        """Returns the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height, ensuring it's greater than zero."""
        if value > 0:
            self.__height = value
        else:
            print('Invalid height. Height must be greater than zero.')

    @property
    def bottomRight(self):
        """Calculates and returns the bottom-right corner as a Point object."""
        return Point(self.__topLeft.x + self.__width, self.__topLeft.y - self.__height)

    @property
    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    @property
    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)

    def translate(self, dx, dy):
        """Moves the rectangle by translating its top-left corner."""
        self.__topLeft.translate(dx, dy)
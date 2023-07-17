#!/usr/bin/python3
"""
Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, inherits from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes an instance of the Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int): x-coordinate of the rectangle's position.
            y (int): y-coordinate of the rectangle's position.
            id (int): ID value for the instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: Area value.
        """
        return self.width * self.height

    def display(self):
        """
        Displays the rectangle as a series of '#' characters on the stdout.
        """
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """
        Assigns arguments to the attributes of the rectangle.

        Args:
            *args: No-keyword arguments for the id, width, height, x, and y attributes.
            **kwargs: Keyword arguments for the attributes of the rectangle.
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.

        Returns:
            str: String representation of the instance.
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"


    @property
    def width(self):
        """
        Getter method for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): New width value.
        """
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): New height value.
        """
        self.__height = value

    @property
    def x(self):
        """
        Getter method for the x attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x attribute.

        Args:
            value (int): New x value.
        """
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the y attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y attribute.

        Args:
            value (int): New y value.
        """
        self.__y = value


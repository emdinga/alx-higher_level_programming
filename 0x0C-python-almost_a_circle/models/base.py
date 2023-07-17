#!/usr/bin/python3
"""
base class
"""
import json
import turtle

class Base:
    """
    Base class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class.

        Args:
            id (int): ID value for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

        @staticmethod
    def from_json_string(json_string):
        """
        Returns the list representation of the JSON string.

        Args:
            json_string (str): JSON string.

        Returns:
            list: List representation of the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

        @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances.

        Returns:
            None
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        json_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(json_list)
        with open(filename, "w") as file:
            file.write(json_string)

        @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.

        Args:
            **dictionary: Double pointer to a dictionary.

        Returns:
            Instance with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

        @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a JSON file.

        Returns:
            list: List of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()
                json_list = cls.from_json_string(json_string)
                return [cls.create(**dictionary) for dictionary in json_list]
        except FileNotFoundError:
            return []

        @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes list_objs to CSV file.

        Args:
            list_objs (list): List of instances.

        Returns:
            None
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            if list_objs is not None:
                for obj in list_objs:
                    writer.writerow(obj.to_csv_row())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes instances from CSV file.

        Returns:
            list: List of instances.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    instance = cls.create(*map(int, row))
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

        @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws all the Rectangles and Squares using the Turtle module.

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.

        Returns:
            None
        """
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")
        screen.setup(width=800, height=600)

        pen = turtle.Turtle()
        pen.speed(2)

        for rect in list_rectangles:
            pen.penup()
            pen.goto(rect.x, rect.y)
            pen.pendown()
            pen.color("blue")
            for _ in range(2):
                pen.forward(rect.width)
                pen.left(90)
                pen.forward(rect.height)
                pen.left(90)

        for square in list_squares:
            pen.penup()
            pen.goto(square.x, square.y)
            pen.pendown()
            pen.color("red")
            for _ in range(4):
                pen.forward(square.size)
                pen.left(90)

        turtle.done()

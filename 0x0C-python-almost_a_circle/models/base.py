#!/usr/bin/python3
""" define base class """

import json
import csv


class Base:
    """Represent the base model class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a new Base instance.

        Args:
            id (int): The identifier for the instance. Defaults to None.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string.

        Returns:
            list: The list of dictionaries represented by the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of instances to a file in JSON format.

        Args:
            list_objs (list): A list of instances to be saved.
        """
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, "w") as file:
            file.write(cls.to_json_string(json_list))

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a file in JSON format.

        Returns:
            list: The list of instances loaded from the file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_list = file.read()
                dict_list = cls.from_json_string(json_list)
                return [cls.create(**d) for d in dict_list]
        except IOError:
            return []

    @classmethod
    def create(cls, **dictionary):
        """
        Create a new instance with the given attributes.

        Returns:
            Base: A new instance with the given attributes.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Save a list of instances to a CSV file.

        Args:
            list_objs (list): A list of instances to be saved.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for rect in list_objs:
                    writer.writerow([rect.id, rect.width, rect.height, rect.x, rect.y])
            elif cls.__name__ == "Square":
                for square in list_objs:
                    writer.writerow([square.id, square.size, square.x, square.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Load a list of instances from a CSV file.

        Returns:
            list: The list of instances loaded from the file.
        """
        filename = cls.__name__ + ".csv"
        instances = []
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                row = [int(x) for x in row]
                if cls.__name__ == "Rectangle":
                    instance = cls(row[1], row[2], row[3], row[4], row[0])
                elif cls.__name__ == "Square":
                    instance = cls(row[1], row[2], row[3], row[0])
                instances.append(instance)
        return instances


#!/usr/bin/python3

"""
Defining a class Base.
"""
import csv
import json
import turtle


class Base():
    """
    A private class variable  __nb_objects
    """
    __nb_objects = 0
    def __init__(self, id=None):
        self.id = id
        if self.id is not None:
            self.id
        else:
            """
            Increment the base class and retrn it as the new id
            """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    """
    Static methods
    """
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None and list_dictionaries == []:
            return "[]"
        """
        Decerialise the list
        """
        json.dumps(list_dictionaries)

    """
    Writting a json representation to a file using json.dump
    It takes in two argments , the file and what is to be dumped.
    This is a class method since it takes the class as the first argument
    """
    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename,"w") as f:
            if list_objs is None:
                f.write("[]")
            f.write(Base.to_json_string(list_objs))

    """
    A static method behaves like a normal method and does not pass an instance or a class
    We use the json.loads() method to convert to string
    """
    @staticmethod
    def from_json_string(json_string):
        if json_string is None and json_string == "[]":
            return []
        json.loads(json_string)

    """
    class method that returns an instance with all attributes already set
    """
    @classmethod
    def create(cls, **dictionary):
        """Return a class instantiated from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
    
    """
    Returns a list of all instances
    """
    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            f = open(filename)
            lst = Base.from_json_string(f.read())
            return [Base.create(**lst)]
        except FileNotFoundError:
            return []

    """
     serializes and deserializes in CSV:
    """
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

        




             
#!/usr/bin/python3
""" a class """


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of a Student instance"""
        if isinstance(attrs, list) and all(isinstance(i, str) for i in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)

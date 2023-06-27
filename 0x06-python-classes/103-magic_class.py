#!/usr/bin/python3

"""Define a MagicClass matching exactly a bytecode."""

import math


class MagicClass:
    """A class that represents a circle and
        provides methods for calculating its area and circumference.

    Attributes:
        __radius (float): The radius of the circle.

    Raises:
        TypeError: If the radius argument is not a number.

    """
    def __init__(self, radius: 0):
        """Creates a MagicClass instance with the given radius.

        Args:
            radius (float): The radius of the circle.

        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self) -> float:
        """Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.

        """
        return (2 ** self.__radius * math.pi)

    def circumference(self) -> float:
        """Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.

        """
        return (2 * math.pi * self.__radius)

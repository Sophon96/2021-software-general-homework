from numbers import Real
from math import pi
from traceback import print_exc


def sphere_volume(radius: Real) -> Real:
    """
    Calculates the volume of a sphere.
    :param radius: The radius of the sphere.
    :return: The volume of the sphere.
    :raises ValueError: If the radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius must be non-negative.")

    return 4/3 * pi * radius


if __name__ == '__main__':
    print("Negative (fail)")
    try:
        print(sphere_volume(-1))
    except ValueError:
        print_exc()
    print("Zero (Success)")
    print(sphere_volume(0))
    print("Positive (Success)")
    print(sphere_volume(3))

from math import sqrt, atan2

import numpy as np


def triangulate(quad):
    a, b, c, d = quad
    yield (a, b, c)
    yield (a, c, d)


def cycle_pairs(l):
    first = l
    second = l[1:] + [l[0]]
    return list(zip(first, second))


def make_angle(x, y, z):
    """
        >>> make_angle(1, 0, 0)
        0.0
        >>> make_angle(0, 1, 1)
        1.0
        >>> make_angle(0, 1, 0)
        0.667
        >>> make_angle(1, 0, 1)
        1.667
    """
    a = (x + y + z) / 3.0
    x, y, z = x - a, y - a, z - a 
    u = x - y / 2 - z / 2
    v = SIN_60 * y - SIN_60 * z
    t = atan2(v, u)
    r = (t / PI)
    return round(r if r >= 0 else r + 2, 3)


def arrange(l):
    """
        >>> arrange([(0, 1, 1), (1, 0, 1), (1, 1, 0)])
        [(1, 1, 0), (0, 1, 1), (1, 0, 1)]
    """
    return sorted(l, key=lambda p: make_angle(*p))


SIN_60 = sqrt(3) / 2
SQRT_3_OVER_2 = sqrt(3) / sqrt(2)
PI = atan2(0, -1)

DIAGONAL_TO_Z = np.array([
    [0.5, -0.5, 0],
    [SIN_60/3, SIN_60/3, -2 * SIN_60/3],
    [-SQRT_3_OVER_2/3, -SQRT_3_OVER_2/3, -SQRT_3_OVER_2/3]
])
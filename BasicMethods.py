import math

def G(y: int, x: int, n: int) -> int:
    """[y, x of the slope's integer part multiplication by a value]

    Args:
        n (int): [the y value of the slope]
        x (int): [the x value of the slope]
        y (int): [the multiplicator]

    Returns:
        int: [Multiplied slope's integer part]
    """
    return math.floor(y / x) * n




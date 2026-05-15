"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40

def bake_time_remaining(completed):
    """Calculates time remaining in baking.

    :param completed: int - completed time of the dish
    :return int - time remaining in baking
    """
    return EXPECTED_BAKE_TIME - completed

def preparation_time_in_minutes(layers):
    """Calculates preperation time.

    :param layers: int - number of layers
    :return int - preperation time
    """
    return layers*2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)


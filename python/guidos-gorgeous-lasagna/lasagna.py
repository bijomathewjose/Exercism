"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME=40
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer
PREPARATION_TIME=2

# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME-elapsed_bake_time
    

    


# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time for N layers.
    
    :param no_of_layers: int - number of layers to add in lasagna
    :return: int - time required to prepare the number of layers in lasagna
        
    """
    return number_of_layers*PREPARATION_TIME

# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """ Calculate total elapsed cooking time (prep + bake) in minutes
    
    :param no_of_layers: int - the number of layers you want to add to the lasagna 
    :param elapsed_baking_time: int - baking time already elapsed
    :return: int - the elapsed time in preparation of lasagna
    
    """
    return preparation_time_in_minutes(number_of_layers)+elapsed_bake_time
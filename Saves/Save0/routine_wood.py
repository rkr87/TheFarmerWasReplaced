from util_math import is_even
from util_plant import plant_entity
from util_routine import basic_routine


def _plant_logic(x, y, size):  # noqa: ARG001
    # Plant either a tree or a bush based on position
    # Args:
    #   x: int  # world x coordinate
    #   y: int  # world y coordinate
    #   size: int | None  # world size (unused)
    # Returns: None
    if is_even(x + y):
        plant_entity(Entities.Tree)
    else:
        plant_entity(Entities.Bush)


def run(x, y, size):
    # Run tree/bush planting routine
    # Args:
    #   x: int  # world x coordinate
    #   y: int  # world y coordinate
    #   size: int  # world size
    # Returns: tuple[int, int]  # drone location after completion
    return basic_routine(x, y, size, _plant_logic)

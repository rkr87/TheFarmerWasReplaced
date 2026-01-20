from util_plant import plant_entity
from util_routine import basic_routine


def _plant_logic(x, y, size):  # noqa: ARG001
    # Execute planting logic for carrots
    #   x: int          # world x coordinate
    #   y: int          # world y coordinate
    #   size: int  # world size
    # Returns: None
    plant_entity(Entities.Carrot, Grounds.Soil)


def run(x, y, size):
    # Run carrot farming routine
    # Args:
    #   x: int          # world x coordinate
    #   y: int          # world y coordinate
    #   size: int  # world size
    # Returns: tuple[int, int]  # drone location after completion
    return basic_routine(x,y, size, _plant_logic)

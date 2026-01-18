from util_math import is_even
from util_plant import plant_entity
from util_routine import basic_routine


def _plant_logic(x, y, size=None):  # noqa: ARG001
    # Execute mixed planting logic based on position and inventory
    # Args:
    #   x: int          # world x coordinate
    #   y: int          # world y coordinate
    #   size: int | None  # world size (unused)
    # Returns: None
    buffer = 500000

    if is_even(x + y) and num_items(Items.Wood) < buffer:
        plant_entity(Entities.Tree)
    elif is_even(x % 2) and num_items(Items.Hay) < buffer:
        plant_entity(Entities.Grass, Grounds.Grassland, False, False)
    else:
        plant_entity(Entities.Carrot, Grounds.Soil)


def run(size):
    # Run wood / grass / carrot farming routine
    # Args:
    #   size: int  # world size
    # Returns: None
    basic_routine(size, _plant_logic)

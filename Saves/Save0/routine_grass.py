from util_plant import plant_entity
from util_routine import basic_routine


def _plant_logic():
    # Execute planting logic for grass
    # Returns: None
    plant_entity(Entities.Grass, Grounds.Grassland, False, False)


def run(size):
    # Run grass farming routine
    # Args:
    #   size: int  # world size
    # Returns: None
    basic_routine(size, _plant_logic, False)

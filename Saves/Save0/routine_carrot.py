from util_plant import plant_entity
from util_routine import basic_routine


def _plant_logic():
    # Execute planting logic for carrots
    # Returns: None
    plant_entity(Entities.Carrot, Grounds.Soil)


def run(size):
    # Run carrot farming routine
    # Args:
    #   size: int  # world size
    # Returns: None
    basic_routine(size, _plant_logic, False)

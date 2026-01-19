from util_harvest import await_harvest
from util_item import water
from util_move import goto_nearest
from util_plant import plant_entity
from util_routine import basic_routine

# coords to harvest per petal count
# Type: list[list[tuple[int, int]]] | None
flowers = [[],[],[],[],[],[],[],[],[]]

def _plant_logic(x, y, size):
    # Plant a sunflower at (x, y)
    # Args:
    #   x: int
    #   y: int
    #   size: int | None  # world size
    # Returns: None
    plant_entity(Entities.Sunflower, Grounds.Soil)
    if x > size - 2:
        water()
    priority = 15 - measure()
    flowers[priority].append((x, y))

def _harvest_flowers(x, y, size):
    # Harvest sunflowers in order of petal count
    # Args:
    #   x: int  # start x coordinate
    #   y: int  # start y coordinate
    #   size: int
    # Returns: None
    for coords in flowers:
        while len(coords) > 0:
            x, y = goto_nearest(coords, x, y, size)
            await_harvest()
            plant_entity(Entities.Carrot, Grounds.Soil)


def run(size):
    # Run sunflower planting and harvesting routine
    # Args:
    #   size: int  # world size
    # Returns: None
    x, y = basic_routine(size, _plant_logic, True, Entities.Sunflower)
    _harvest_flowers(x, y, size)

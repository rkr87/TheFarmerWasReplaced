from util_harvest import await_harvest
from util_item import water
from util_list import build_grid
from util_move import goto_nearest
from util_plant import plant_entity
from util_routine import basic_routine

# Grid storing petal measurement per coordinate
# Type: list[list[int]] | None
flowers = None


def _plant_logic(x, y, size=None):
    # Plant a sunflower at (x, y) and optionally water it
    # Args:
    #   x: int
    #   y: int
    #   size: int | None  # world size
    # Returns: None
    size = size or get_world_size()
    plant_entity(Entities.Sunflower, Grounds.Soil)
    if x > size - 3:
        water()
    flowers[x][y] = measure()


def _get_harvest_items(size):
    # Get list of flower coordinates grouped by petal count
    # Args:
    #   size: int  # world size
    # Returns: list[list[tuple[int, int]]]  # coords to harvest per petal count
    harvest_list = []
    for i in range(15, 6, -1):
        i_list = []
        for x in range(size):
            for y in range(size):
                if flowers[x][y] == i:
                    i_list.append((x, y))
        harvest_list.append(i_list)
    return harvest_list


def _harvest_flowers(x, y, size):
    # Harvest sunflowers in order of petal count
    # Args:
    #   x: int  # start x coordinate
    #   y: int  # start y coordinate
    #   size: int
    # Returns: None
    for coords in _get_harvest_items(size):
        while len(coords) > 0:
            x, y = goto_nearest(coords, x, y, size)
            await_harvest(None)
            plant_entity(Entities.Carrot, Grounds.Soil)


def run(size):
    # Run sunflower planting and harvesting routine
    # Args:
    #   size: int  # world size
    # Returns: None
    global flowers
    flowers = flowers or build_grid(size)
    x, y = basic_routine(size, _plant_logic, True, Entities.Sunflower)
    _harvest_flowers( x, y, size)

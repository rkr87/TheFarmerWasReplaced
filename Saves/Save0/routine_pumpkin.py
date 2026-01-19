from util_harvest import await_harvest
from util_item import await_water
from util_move import goto_nearest
from util_plant import plant_entity
from util_routine import basic_routine

# List of coordinates where pumpkins failed to plant
# Type: list[tuple[int, int]]
dead = []


def _plant_logic():
    # Attempt to plant a pumpkin at a location
    # Returns: bool  # True if planted item
    return plant_entity(Entities.Pumpkin, Grounds.Soil, True)


def _dead_logic(x, y, size=None):  # noqa: ARG001
    # Handle failed pumpkin locations
    # Args:
    #   x: int
    #   y: int
    #   size: int | None  # world size (unused)
    # Returns: None
    if _plant_logic():
        dead.append((x, y))

def _replant_pumpkins(x, y, size):
    # Replant pumpkins at previously failed locations
    # Args:
    #   x: int  # current x coordinate
    #   y: int  # current y coordinate
    #   size: int
    # Returns: tuple[int, int]  # drone location after completion
    global dead
    still_dead = []
    while len(dead) > 0:
        x, y = goto_nearest(dead, x, y, size)
        await_water(Entities.Pumpkin)
        if _plant_logic():
            still_dead.append((x, y))
    dead = still_dead
    return x, y


def run(size):
    # Run full pumpkin farming routine
    # Args:
    #   size: int  # world size
    # Returns: None
    basic_routine(size, _plant_logic, False, Entities.Pumpkin)
    x, y = basic_routine(size, _dead_logic, True, Entities.Pumpkin)
    while len(dead) > 0:
        x, y = _replant_pumpkins(x, y, size)
    await_harvest()

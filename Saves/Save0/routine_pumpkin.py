from util_harvest import await_harvest
from util_item import water
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

def _quick_grow():
    # Water pumpkin once during growth if needed
    # Returns: bool  # True if watering occurred
    quick_grow = True
    while get_entity_type() == Entities.Pumpkin and not can_harvest():
        if quick_grow:
            water()
            quick_grow = False
    return quick_grow

def _replant_pumpkins(x, y, size):
    # Replant pumpkins at previously failed locations
    # Args:
    #   x: int  # current x coordinate
    #   y: int  # current y coordinate
    #   size: int
    # Returns: tuple[int, int]  # drone location after completion
    global dead
    still_dead = []
    use_water = False
    if len(dead) <= 5:
        use_water = True
    while len(dead) > 0:
        x, y = goto_nearest(dead, x, y, size)
        quick_grow = _quick_grow()
        if not _plant_logic():
            continue
        still_dead.append((x, y))
        if use_water and quick_grow:
            water()
    dead = still_dead
    return x, y


def run(size):
    # Run full pumpkin farming routine
    # Args:
    #   size: int  # world size
    # Returns: None
    global dead
    dead = []
    basic_routine(size, _plant_logic, False, Entities.Pumpkin)
    x, y = basic_routine(size, _dead_logic, True, Entities.Pumpkin)
    while len(dead) > 0:
        x, y = _replant_pumpkins(x, y, size)
    await_harvest(None)

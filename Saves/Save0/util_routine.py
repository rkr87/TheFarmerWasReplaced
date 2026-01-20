from util_distance import cycle_steps
from util_harvest import try_harvest
from util_item import item_priority
from util_move import move_sequence


def basic_routine(x, y, size, function, skip_entity=None):
    # Execute a basic farming routine
    # Args:
    #   x: int
    #   y: int
    #   size: int  # world/grid size
    #   plant_func: Callable[..., Any]  # function to plant an entity
    #   skip_entity: Entities | None  # entity type to skip harvesting
    # Returns: tuple[int, int]  # final x, y position
    for _ in cycle_steps(size):
        try_harvest(skip_entity)
        function(x, y, size)
        x, y = move_sequence(x, y, size)
    return x, y


def select_routine(routines):
    # Select a routine based on item priority
    # Args:
    #   routines: list[list[Any]]  # [routine, item, min_threshold, increment]
    # Returns: Callable[..., Any]  # selected routine function
    current_priority = None
    current_index = None
    for i in range(len(routines)):
        routine = routines[i]
        priority = item_priority(routine[1], routine[2], routine[3])
        if priority == None:
            continue
        if priority == 1:
            return routines[i][0]
        if current_priority == None or priority < current_priority:
            current_priority = priority
            current_index = i

    return routines[current_index][0]

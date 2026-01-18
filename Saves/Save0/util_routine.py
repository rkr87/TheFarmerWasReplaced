from util_harvest import try_harvest
from util_item import item_priority
from util_move import goto_coord, move_sequence


def basic_routine(size, plant_func, req_loc=True, skip_entity=None):
    # Execute a basic farming routine
    # Args:
    #   size: int  # world/grid size
    #   plant_func: Callable[..., Any]  # function to plant an entity
    #   req_loc: bool  # whether plant_func requires x, y coordinates
    #   skip_entity: Entities | None  # entity type to skip harvesting
    # Returns: tuple[int, int]  # final x, y position
    x, y = goto_coord(0, 0, get_pos_x(), get_pos_y(), size)
    complete = False
    while not complete:
        try_harvest(skip_entity)
        if req_loc:
            plant_func(x, y, size)
        else:
            plant_func()
        x, y = move_sequence(x, y, size)
        complete = (x, y) == (0, 0)
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

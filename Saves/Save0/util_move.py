from util_distance import get_distance_x, get_distance_y


def _move_distance(steps, direction):
    # Move a fixed number of steps in one direction
    # Args:
    #   steps: int
    #   direction: Direction
    # Returns: None
    if steps == 0:
        return
    for _ in range(steps):
        move(direction)


def move_sequence(current_x, current_y, size):
    # Perform a fixed movement pattern and update position
    # Args:
    #   current_x: int
    #   current_y: int
    #   size: int  # world/grid size
    # Returns: tuple[int, int]  # updated x, y
    move(North)

    # Wrap horizontally when crossing top edge
    if current_y == size - 1:
        move(East)
        current_x = get_pos_x()
    current_y = get_pos_y()
    return current_x, current_y


def goto_coord(target_x, target_y, current_x, current_y, size):
    # Move directly to a target coordinate
    # Args:
    #   target_x: int
    #   target_y: int
    #   current_x: int
    #   current_y: int
    #   size: int
    # Returns: tuple[int, int]  # updated x, y
    if current_x != target_x:
        steps, direction = get_distance_x(current_x, target_x, size)
        _move_distance(steps, direction)
        current_x = get_pos_x()
    if current_y != target_y:
        steps, direction = get_distance_y(current_y, target_y, size)
        _move_distance(steps, direction)
        current_y = get_pos_y()
    return current_x, current_y


def goto_distance(distance_x, distance_y, current_x, current_y):
    # Move using precomputed (steps, direction) tuples
    # Args:
    #   distance_x: tuple[int, Direction]
    #   distance_y: tuple[int, Direction]
    #   current_x: int
    #   current_y: int
    # Returns: tuple[int, int]  # updated x, y
    if distance_x[0] != 0:
        _move_distance(distance_x[0], distance_x[1])
        current_x = get_pos_x()
    if distance_y[0] != 0:
        _move_distance(distance_y[0], distance_y[1])
        current_y = get_pos_y()
    return current_x, current_y


def _quick_select(num_coords, size):
    # Calculate quick exit threshold based on world size and number of coords.
    # Args:
    #    num_coords: int - number of coordinates left to check
    #    size: int - world/grid size
    #    base: int - base minimum threshold
    # Returns: int - dynamic quick select threshold
    max_coords = size * size
    base_threshold = (size // 2) * .25
    coord_factor = 1 - (num_coords / max_coords)
    threshold = base_threshold / coord_factor
    return max(1, threshold)  # ensure at least 1


def goto_nearest(coords, x, y, size, remove_coord=True):
    # Move to the nearest coordinate and optionally remove it from the list
    # Args:
    #   coords: list[tuple[int, int]]  # list of target coordinates
    #   x: int
    #   y: int
    #   size: int  # world/grid size
    #   remove_coord: int = True  # remove selected coord from list
    # Returns: tuple[int, int]  # updated x, y
    num_coords = len(coords)
    quick_select = _quick_select(num_coords, size)
    nearest = None, None, -1, size  # (dist_x, dist_y, index, total_distance)
    for i in range(num_coords):
        distance_x = get_distance_x(x, coords[i][0], size)
        distance_y = get_distance_y(y, coords[i][1], size)
        total_distance = distance_x[0] + distance_y[0]
        if total_distance >= nearest[3]:
            continue
        nearest = distance_x, distance_y, i, total_distance

        if nearest[3] <= quick_select:
            break
    do_move = goto_distance(nearest[0], nearest[1], x, y)
    if remove_coord:
        coords.pop(nearest[2])
    return do_move

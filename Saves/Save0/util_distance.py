def _get_distance(current, target, size):
    # Compute shortest wrap-around distance between two coordinates
    # Args:
    #   current: int
    #   target: int
    #   size: int  # world/grid size
    # Returns: tuple[int, int]  # forward distance, backward distance
    return (target - current) % size, (current - target) % size


def get_distance_x(curr_x, tar_x, size):
    # Compute shortest horizontal distance and direction
    # Args:
    #   curr_x: int
    #   tar_x: int
    #   size: int  # world/grid width
    # Returns: tuple[int, Direction]  # distance, East or West
    distance = _get_distance(curr_x, tar_x, size)
    if distance[0] < distance[1]:
        return distance[0], East
    return distance[1], West


def get_distance_y(curr_y, tar_y, size):
    # Compute shortest vertical distance and direction
    # Args:
    #   curr_y: int
    #   tar_y: int
    #   size: int  # world/grid height
    # Returns: tuple[int, Direction]  # distance, North or South
    distance = _get_distance(curr_y, tar_y, size)
    if distance[0] < distance[1]:
        return distance[0], North
    return distance[1], South

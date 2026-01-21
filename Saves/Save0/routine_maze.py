from util_item import apply_weird_substance
from util_move import move_chain


def _solve_maze(x, y, size): # noqa: ARG001
    # Basic maze solver
    # Args:
    #   x: int  # start x coordinate
    #   y: int  # start y coordinate
    #   size: int
    # Returns: tuple[int, int]  # drone location after completion
    attempt_move  = 0
    while get_entity_type() != Entities.Treasure:
        attempt_move = move_chain(attempt_move)

    harvest()
    return get_pos_x(), get_pos_y()


def run(x, y, size):
    # Run maze solver
    # Args:
    #   x: int
    #   y: int
    #   size: int  # world size
    # Returns: tuple[int, int]  # drone location after completion
    plant(Entities.Bush)
    substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
    apply_weird_substance(substance)
    return _solve_maze(x, y, size)

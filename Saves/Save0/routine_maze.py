from util_harvest import await_harvest
from util_item import apply_weird_substance
from util_move import move_priority_right


def _prepare_maze(size):
    await_harvest()
    plant(Entities.Bush)
    substance = size * 2**(num_unlocked(Unlocks.Mazes) - 1)
    apply_weird_substance(substance)

def _solve_maze():
    current_face  = 0
    while get_entity_type() != Entities.Treasure:
        current_face = move_priority_right(current_face)
    harvest()
    return get_pos_x(), get_pos_y()


def run(x, y, size): # noqa: ARG001
    _prepare_maze(size)
    return _solve_maze()

import routine_carrot
import routine_grass
import routine_maze
import routine_pumpkin
import routine_sunflower
import routine_wood
from util_routine import select_routine

# Routine configuration list
#   routine_module,                   # module with .run(size: int) -> None
#   item: Items,                      # item produced by routine
#   target_amount: int,               # stop condition / goal
#   priority_increment: int | None    # priority increment for over target item
routine_def = [
    [routine_grass, Items.Hay, 500000, 5000],
    [routine_wood, Items.Wood, 500000, 5000],
    [routine_carrot, Items.Carrot, 500000, 5000],
    [routine_pumpkin, Items.Pumpkin, 500000, 5000],
    [routine_sunflower, Items.Power, 20000, None],
]

while True:
    routine = select_routine(routine_def)
    if routine == routine_maze:
        size = 5
    else:
        size = get_world_size()
    routine.run(size)

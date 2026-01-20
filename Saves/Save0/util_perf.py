from util_func import callable_func
from util_move import goto_coord, goto_nearest


def _function_timer(function):
    # Measure execution time (ticks) of a function
    # Args:
    #   function: Callable[..., Any]
    # Returns: tuple[Any, int]  # (function result, elapsed ticks)
    start_ticks = get_tick_count()
    return function(), get_tick_count() - start_ticks


def get_function_ticks(function, args):
    # Get execution ticks and result of a function call with arguments
    # Args:
    #   function: Callable[..., Any]
    #   args: list[Any]  # arguments for function
    # Returns: dict[str, Any]  # {"function": str, "result": Any, "ticks": int}
    str_func = str(function) + "(" + str(args)[1:-1] + ")"
    func = callable_func(function, args)
    function_ticks = _function_timer(func)
    return {
        "function": str_func,
        "result": function_ticks[0],
        "ticks": function_ticks[1],
    }


# List of test functions with arguments
# Type: list[tuple[Callable[..., Any], list[Any]]]
functions = [
    (goto_nearest, [[(0, 1)], 0, 0, 32]),
]

# Run tests and print timing information
for f, a in functions:
    x, y = goto_coord(0, 0, get_pos_x(), get_pos_y(), get_world_size())
    quick_print(get_function_ticks(f, a))
    for _ in range(2000):
        pass

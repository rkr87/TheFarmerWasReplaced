# Series of function wrappers for n args
# Args:
#   function: Callable[[Any], Any]
#   args: list[Any]  # length 1
# Returns: Callable[[], Any]
def _func_n0(function, args):  # noqa: ARG001
    return function


def _func_n1(function, args):
    def do_work():
        return function(args[0])

    return do_work


def _func_n2(function, args):
    def do_work():
        return function(args[0], args[1])

    return do_work


def _func_n3(function, args):
    def do_work():
        return function(args[0], args[1], args[2])

    return do_work


def _func_n4(function, args):
    def do_work():
        return function(args[0], args[1], args[2], args[3])

    return do_work


def _func_n5(function, args):
    def do_work():
        return function(args[0], args[1], args[2], args[3], args[4])

    return do_work

# List of internal function wrappers by argument count
# Type: list[Callable[..., Any]]
_funcs = [_func_n0, _func_n1, _func_n2, _func_n3, _func_n4, _func_n5]


def callable_func(function, args=None):
    # Return callable function with arguments bound
    # Args:
    #   function: Callable[..., Any]
    #   args: list[Any] | None  # arguments to bind
    # Returns: Callable[..., Any]
    if args == None:
        args = []
    func_call = _funcs[len(args)]
    return func_call(function, args)

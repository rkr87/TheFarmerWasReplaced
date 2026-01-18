def build_grid(size):
    # Build a 2D grid initialized with zeros
    # Args:
    #   size: int  # width and height of the square grid
    # Returns: list[list[int]]  # 2D grid of zeros
    result = []
    for x in range(size):
        result.append([])
        for _ in range(size):
            result[x].append(0)
    return result

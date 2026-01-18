def item_priority(item, min_threshold, increment=None):
    # Determine item priority based on count and thresholds
    # Args:
    #   item: Items  # item type to check
    #   min_threshold: int  # minimum count for normal priority
    #   increment: int | None  # step increment for higher priority
    # Returns: int | None  # priority level or None if no increment
    item_count = num_items(item)
    if item_count < min_threshold:
        return 1
    if increment == None:
        return None
    return ((item_count - min_threshold) // increment) + 2


def water():
    # Use water if available
    # Returns: bool  # True if used, False otherwise
    if num_items(Items.Water) > 0:
        use_item(Items.Water)
        return True
    return False


def fertilise(amount=1):
    # Use fertilizer if available
    # Args:
    #   amount: int  # amount of fertilizer to use
    # Returns: bool  # True if used, False otherwise
    if num_items(Items.Fertilizer) > 0:
        use_item(Items.Fertilizer, amount)
        return True
    return False

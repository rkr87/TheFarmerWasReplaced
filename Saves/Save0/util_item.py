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


def _use_item(item, amount = 1):
    if num_items(item) > 0:
        use_item(item, amount)
        return True
    return False

def water(amount = 1):
    # Use water if available
    # Returns: bool  # True if used, False otherwise
    return _use_item(Items.Water, amount)

def await_water(entity=None):
    # Water entity and wait until harvestable
    # Returns: bool  # True if watering occurred
    quick_grow = True
    while not can_harvest() and entity in {None, get_entity_type()}:
        if quick_grow:
            water()
            quick_grow = False
    return quick_grow


def fertilise(amount=1):
    # Use fertilizer if available
    # Args:
    #   amount: int  # amount of fertilizer to use
    # Returns: bool  # True if used, False otherwise
    return _use_item(Items.Fertilizer, amount)

def apply_weird_substance(amount=1):
    # Use weird substance if available
    # Args:
    #   amount: int  # amount of fertilizer to use
    # Returns: bool  # True if used, False otherwise
    return _use_item(Items.Weird_Substance, amount)

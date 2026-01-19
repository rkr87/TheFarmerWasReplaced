from util_item import water


def try_harvest(skip_entity=None):
    # Attempt to harvest if ready, skipping specified entity
    # Args:
    #   skip_entity: Entities | None  # entity type to skip
    # Returns: None
    if skip_entity == get_entity_type():
        return
    if can_harvest():
        harvest()

def await_harvest(skip_entity=None, add_water = True):
    # Wait until harvesting is possible and harvest, skipping specified entity
    # Args:
    #   skip_entity: Entities | None  # entity type to skip
    # Returns: None
    if skip_entity == get_entity_type():
        return
    while not can_harvest():
        if add_water:
            water()
            add_water = False
    harvest()

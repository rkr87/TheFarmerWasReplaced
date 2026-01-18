def _prepare_ground(ground):
    # Prepare the ground for planting if needed
    # Args:
    #   ground: Grounds | None  # desired ground type
    # Returns: None
    if ground != None and ground != get_ground_type():
        till()

def _should_plant(entity, requires_replant):
    # Determine if planting should occur based on replant requirement
    # Args:
    #   entity: Entities
    #   requires_replant: bool
    # Returns: bool  # True if planting should proceed
    return not requires_replant or get_entity_type() != entity

def plant_entity(
    entity, ground=None, requires_replant=False, requires_seeding=True
):
    # Plant an entity if conditions are met
    # Args:
    #   entity: Entities  # entity type to plant
    #   ground: Grounds | None  # optional ground type to prepare
    #   requires_replant: bool  # only plant over different entities
    #   requires_seeding: bool  # whether seeding is required
    # Returns: bool  # True if planted, False otherwise
    _prepare_ground(ground)
    if requires_seeding and _should_plant(entity, requires_replant):
        plant(entity)
        return True
    return False

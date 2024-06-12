class OwnerNotFoundException(Exception):
    def __init__(self, owner_id: int):
        self.owner_id = owner_id
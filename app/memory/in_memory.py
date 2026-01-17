class InMemoryMemory:
    """
    A simple in-memory key-value store for storing user data.
    """

    def __init__(self):
        self.store_data = {}

    def store(self, user_id: str, value: str):
        self.store_data.setdefault(user_id, []).append(value)

    def retrieve(self, user_id: str):
        return self.store_data.get(user_id, [])

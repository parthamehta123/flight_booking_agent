class InMemoryMemory:
    """
    Simple in-memory memory store for tests and CI.
    Acts as a drop-in replacement for VectorMemory.
    """

    def __init__(self):
        self.store_data = {}

    def store(self, user_id: str, text: str):
        if user_id not in self.store_data:
            self.store_data[user_id] = []
        self.store_data[user_id].append(text)

    def get(self, user_id: str):
        return self.store_data.get(user_id, [])

    def clear(self, user_id: str):
        self.store_data.pop(user_id, None)

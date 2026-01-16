import chromadb
from app.config.settings import settings


class VectorMemory:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=settings.chroma_path)
        self.collection = self.client.get_or_create_collection("memory")

    def store(self, user_id: str, text: str):
        self.collection.add(documents=[text], ids=[f"{user_id}-{hash(text)}"])

    def recall(self, query: str, n: int = 3):
        return self.collection.query(query_texts=[query], n_results=n)

import chromadb
from app.config.settings import settings


class VectorMemory:
    def __init__(self):
        self.client = chromadb.PersistentClient(path=settings.chroma_path)

        # Optional but recommended: isolate by environment
        collection_name = f"memory_{settings.env}"

        self.collection = self.client.get_or_create_collection(collection_name)

    def store(self, user_id: str, text: str):
        """
        Store or update memory for a user.
        This is idempotent: one memory entry per user.
        """
        self.collection.upsert(
            documents=[text],
            ids=[user_id],
            metadatas=[{"user_id": user_id}],
        )

    def recall(self, user_id: str) -> str | None:
        """
        Retrieve the latest memory for a user.
        """
        result = self.collection.get(ids=[user_id])
        docs = result.get("documents")

        if docs and len(docs) > 0:
            return docs[0]

        return None

    def debug_dump(self) -> list[str]:
        """
        Helper for smoke tests/debugging.
        Returns all stored documents.
        """
        result = self.collection.get()
        return result.get("documents", [])

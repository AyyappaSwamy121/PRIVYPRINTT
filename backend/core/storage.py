"""Storage abstraction placeholders for local and S3 backends."""


class StorageService:
    """TODO: Implement storage adapter methods in Sprint B."""

    def save(self, _path: str, _content: bytes) -> str:
        raise NotImplementedError

    def open(self, _path: str) -> bytes:
        raise NotImplementedError

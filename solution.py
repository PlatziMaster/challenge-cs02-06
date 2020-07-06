"""Solution by <USERNAME>."""


class Set:
    """Set implementation."""

    def __init__(self):
        """Initializes the set."""
        self.data = set()

    def add(self, k: int) -> None:
        """Add k into the set. If k already exists in the set, do nothing."""
        self.data.add(k)

    def remove(self, k: int) -> None:
        """Removes k from the set if exists, else do nothing."""
        self.data.discard(k)

    def contains(self, k: int) -> bool:
        """Returns whether k is present in the set or not."""
        return k in self.data

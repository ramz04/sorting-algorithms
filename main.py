from typing import Any


class Queue:
    def __init__(self) -> None:
        self.items: list[Any] = []

    def push(self, item: Any) -> None:
        self.items.append(item)

    def pop(self) -> Any:
        if not self.items:
            return None
        return self.items.pop(0)

    def peek(self) -> Any:
        if not self.items:
            return None
        return self.items[0]

    def size(self) -> int:
        return len(self.items)

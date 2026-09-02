from typing import Any


class Stack:
    def __init__(self) -> None:
        self.items: list[Any] = []

    def push(self, item: Any) -> None:
        self.items.append(item)

    def size(self) -> int:
        return len(self.items)

    def pop(self) -> Any:
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None

    def peek(self) -> Any:
        if len(self.items) > 0:
            return self.items[len(self.items) - 1]
        else:
            return None
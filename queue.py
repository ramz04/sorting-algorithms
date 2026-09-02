from typing import Any


class Queue:
    def __init__(self) -> None:
        self.items: list[Any] = []

    def push(self, item: Any) -> None:
        self.items.insert(0, item)

    def pop(self) -> Any:
        if len(self.items) == 0:
            return None
        temp = self.items[-1]
        del self.items[-1]
        return temp

    def peek(self) -> Any:
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self) -> int:
        return len(self.items)

    def search_and_remove(self, item: Any) -> Any:
        if item not in self.items:
            return None
        self.items.remove(item)
        return item

    def __repr__(self) -> str:
        return f"[{', '.join(self.items)}]"

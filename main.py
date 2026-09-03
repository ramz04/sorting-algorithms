from typing import Any


class Node:
    val: Any
    next: Any

    def __init__(self, val: Any) -> None:
        self.val = val
        self.next = None
        

    def set_next(self, node: "Node") -> None:
        self.next = node

    # don't touch below this line

    def __repr__(self) -> str:
        return self.val
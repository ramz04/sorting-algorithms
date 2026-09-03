from typing import Any


class Node:
    def __init__(self, val: Any) -> None:
        # The payload a node holds.
        self.val = val
        # Link to the next node; None means this is the tail.
        self.next: "Node | None" = None

    def set_next(self, node: "Node | None") -> None:
        # Setter: point this node's next link at another node.
        self.next = node

    def __repr__(self) -> str:
        # Print the node as its value, e.g. "Major Marquis Warren".
        return self.val

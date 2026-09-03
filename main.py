from node import Node


class LinkedList:
    def add_to_head(self, node: Node) -> None:
        # Empty list: the new node doubles as head and tail.
        if self.head is None:
            self.tail = node

        # Link the new node to the current head (None if list was empty).
        node.next = self.head

        # The new node is now the head of the list.
        self.head = node

    def add_to_tail(self, node: Node) -> None:
        # Empty list: the new node becomes the first (and last) element.
        if self.head is None:
            self.head = node
            self.tail = node
            return

        # Link the current tail to the new node (O(1), no full-list walk).
        self.tail.set_next(node)
        # The new node is now the tail of the list.
        self.tail = node

    # don't touch below this line

    def __init__(self) -> None:
        # A brand-new list has no nodes yet.
        self.head: Node | None = None
        self.tail = None

    def __iter__(self):
        # Start at the head, yield each node, then follow the next link
        # until we fall off the end (node is None).
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        # Collect every node's value and join them with arrows.
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)

from node import Node


class LinkedList:
    def add_to_head(self, node: Node) -> None:
        # Link the new node to the current head (None if list was empty).
        node.next = self.head

        # The new node is now the head of the list.
        self.head = node
    
    def add_to_tail(self, node: Node) -> None:
        # Empty list: the new node becomes the first element.
        if self.head is None:
            self.head = node
            return

        # Start walking from the head.
        current = self.head
        # Advance until we reach the last node (its next is None).
        while current.next is not None:
            current = current.next
        # Link the last node to the new node.
        current.next = node

    # don't touch below this line

    def __init__(self) -> None:
        # A brand-new list has no nodes yet.
        self.head: Node | None = None

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

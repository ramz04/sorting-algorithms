from node import Node


class LLQueue:

    def remove_from_head(self) -> Node | None:
        # Empty queue: nothing to remove.
        if self.head is None:
            return None

        # Remember the node being removed.
        removed_head = self.head
        # The head is now the old head's successor (None if it was the last node).
        self.head = removed_head.next
        # If the queue is now empty, there is no tail anymore.
        if self.head is None:
            self.tail = None
        # Detach the removed node so it isn't still linked into the queue.
        removed_head.set_next(None)
        return removed_head
    
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

        assert self.tail is not None

        # Link the current tail to the new node (O(1), no full-list walk).
        self.tail.set_next(node)
        # The new node is now the tail of the list.
        self.tail = node

    # don't touch below this line

    def __init__(self) -> None:
        # A brand-new list has no nodes yet.
        self.head: Node | None = None
        self.tail: Node | None = None

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

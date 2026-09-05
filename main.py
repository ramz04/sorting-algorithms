from typing import Any

class BSTNode:
    def __init__(self, val: Any = None) -> None:
        # Child pointers; a fresh node has no children yet.
        self.left: "BSTNode | None" = None
        self.right: "BSTNode | None" = None
        # The value this node holds (None marks an empty root).
        self.val = val

    def get_min(self) -> Any:
        # Empty tree: there is no minimum.
        if self.val is None:
            return None

        # No left child: this node holds the smallest value.
        if self.left is None:
            return self.val
        # Otherwise the minimum is in the left subtree.
        return self.left.get_min()

    def get_max(self) -> Any:
        # Empty tree: there is no maximum.
        if self.val is None:
            return None

        # No right child: this node holds the largest value.
        if self.right is None:
            return self.val
        # Otherwise the maximum is in the right subtree.
        return self.right.get_max()
            
    def insert(self, val: Any) -> None:
        # Empty root: place the value here and stop.
        if self.val is None:
            self.val = val
            return

        # Duplicate: do nothing (BST keeps unique values).
        if self.val == val:
            return

        # Smaller value goes left.
        if val < self.val:
            if self.left is None:
                # Empty left slot: create a new node here.
                self.left = BSTNode(val)
            else:
                # Otherwise recurse into the left subtree.
                self.left.insert(val)
        # Larger value goes right.
        elif val > self.val:
            if self.right is None:
                # Empty right slot: create a new node here.
                self.right = BSTNode(val)
            else:
                # Otherwise recurse into the right subtree.
                self.right.insert(val)
from main import BSTNode


def ref_implementation(bst: BSTNode, val) -> None:
    if bst.val is None:
        bst.val = val
        return
    if val == bst.val:
        return
    if val < bst.val:
        if bst.left is None:
            bst.left = BSTNode(val)
        else:
            ref_implementation(bst.left, val)
    elif val > bst.val:
        if bst.right is None:
            bst.right = BSTNode(val)
        else:
            ref_implementation(bst.right, val)


def ref_inorder(bst: BSTNode, result: list) -> list:
    if bst is not None:
        ref_inorder(bst.left, result)
        result.append(bst.val)
        ref_inorder(bst.right, result)
    return result

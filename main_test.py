import pytest
from main import BSTNode
from user import get_users

run_cases = [
    pytest.param(5, "Blake#0", "Carrell#14"),
    pytest.param(10, "Ricky#1", "Vennett#29"),
]

submit_cases = [
    pytest.param(15, "Shelley#2", "George#42", marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("num_users", "min_user", "max_user"), run_cases + submit_cases
)
def test_min_max(num_users, min_user, max_user):
    users = get_users(num_users)
    bst = BSTNode()
    for user in users:
        bst.insert(user)
    print("\n=====================================")
    print("Tree:")
    print("-------------------------------------")
    print_tree(bst)
    print("-------------------------------------\n")
    print(f"Expected min: {min_user}, max: {max_user}")
    actual_min = bst.get_min()
    actual_max = bst.get_max()
    print(f"Actual min: {actual_min.user_name}, max: {actual_max.user_name}")
    assert actual_max.user_name == max_user
    assert actual_min.user_name == min_user


def print_tree(bst_node):
    lines = []
    format_tree_string(bst_node, lines)
    print("\n".join(lines))


def format_tree_string(bst_node, lines, level=0):
    if bst_node is not None:
        format_tree_string(bst_node.right, lines, level + 1)
        lines.append(" " * 4 * level + "> " + str(bst_node.val))
        format_tree_string(bst_node.left, lines, level + 1)

import pytest
from main import LLQueue, Node

run_cases = [
    pytest.param(
        ["Rick", "Cliff", "Sharon", "Jay", "Roman", "Squeaky"],
        ["Cliff", "Sharon", "Jay", "Roman", "Squeaky"],
        "Rick",
        "Squeaky",
    ),
    pytest.param(
        ["Cliff", "Sharon", "Jay", "Roman", "Squeaky"],
        ["Sharon", "Jay", "Roman", "Squeaky"],
        "Cliff",
        "Squeaky",
    ),
]

submit_cases = [
    pytest.param([], [], None, None, marks=pytest.mark.submit),
    pytest.param(["Jay"], [], "Jay", None, marks=pytest.mark.submit),
    pytest.param(
        ["Roman", "Squeaky"],
        ["Squeaky"],
        "Roman",
        "Squeaky",
        marks=pytest.mark.submit,
    ),
    pytest.param(["Squeaky"], [], "Squeaky", None, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("items", "expected_state", "expected_head", "expected_tail"),
    run_cases + submit_cases,
)
def test_remove_from_head(items, expected_state, expected_head, expected_tail):
    linked_list = LLQueue()
    for item in items:
        linked_list.add_to_tail(Node(item))

    print("\n---------------------------------")
    print(f"Linked List Queue: {linked_list}")
    print("Removing Head...\n")
    head = linked_list.remove_from_head()
    tail = linked_list.tail
    result = linked_list_to_list(linked_list)
    print(f"Expected List: {expected_state}")
    print(f"  Actual List: {result}\n")
    assert result == expected_state
    print(f"Expected Removed Head: {expected_head}")
    print(f"  Actual Removed Head: {head}\n")
    assert (head is None and expected_head is None) or head.val == expected_head
    print(f"Expected Tail: {expected_tail}")
    print(f"  Actual Tail: {tail}\n")
    assert (tail is None and expected_tail is None) or tail.val == expected_tail
    if head is not None:
        print("Expected Removed Head's Next Node: None")
        print(f"         Actual Removed Head Next: {head.next}\n")
        assert head.next is None


def linked_list_to_list(linked_list):
    result = []
    for node in linked_list:
        result.append(node.val)
    return result

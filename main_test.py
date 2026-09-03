import random
import time

import pytest
from main import LinkedList, Node

run_cases = [
    pytest.param(10, "Patrick Bateman", "Paul Allen"),
    pytest.param(100, "Paul Allen", "Paul Allen"),
    pytest.param(1000, "Paul Allen", "Paul Allen"),
    pytest.param(10000, "Patrick Bateman", "Paul Allen"),
]

submit_cases = [
    pytest.param(12000, "Paul Allen", "Paul Allen", marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    ("num_items", "first_item", "last_item"), run_cases + submit_cases
)
def test_linked_list_queue(num_items, first_item, last_item):
    print("\n---------------------------------")
    print(f"Adding {num_items} job candidates to a linked list's head")
    linked_list = LinkedList()
    linked_list2 = LinkedList()
    timeout = 1.5
    try:
        start = time.time()
        for item in get_items(num_items):
            linked_list.add_to_head(Node(item))

        print(f"Adding {num_items} job candidates to a linked list's tail")
        for item in get_items(num_items):
            linked_list2.add_to_tail(Node(item))
        end = time.time()

        print(f"Expecting to complete in less than {timeout * 1000} milliseconds")
        assert (end - start) < timeout, (
            f"Test took too long ({(end - start) * 1000} milliseconds). Speed it up!"
        )
        print(f"Test completed in less than {timeout * 1000} milliseconds!")

        print("\nChecking the first linked list")
        check_links(linked_list, first_item, last_item, num_items)
        print("\nChecking the second linked list")
        check_links(linked_list2, last_item, first_item, num_items)
    finally:
        cleanup_list(linked_list)
        cleanup_list(linked_list2)


def get_items(num):
    random.seed(1)
    options = ["Patrick Bateman", "Paul Allen", "Evelyn Williams", "Luis Carruthers"]
    items = []
    for _ in range(num):
        option_i = random.randint(0, len(options) - 1)
        items.append(options[option_i])
    return items


def check_links(llist, head, tail, expected_length):
    print(f"Expected Head: {head}")
    print(f"Actual Head: {llist.head}")
    assert head == llist.head.val, (
        "The linked list's head node does not have the expected value. "
        "Check if nodes added to the head are set as the new head node"
    )
    print(f"Expected Tail: {tail}")
    print(f"Actual Tail: {llist.tail}")
    assert tail == llist.tail.val, (
        "The linked list's tail node does not have the expected value. "
        "Check if nodes added to the tail are set as the new tail node"
    )

    actual_length = 0
    for _ in llist:
        actual_length += 1
    print(f"Expected Length: {expected_length}")
    print(f"Actual Length: {actual_length}")
    assert expected_length == actual_length, (
        "The linked list is not the expected length of linked nodes. "
        "Check if added nodes are set as the new head or tail"
    )


def cleanup_list(llist):
    current = llist.head
    while current is not None:
        next_node = current.next
        current.next = None
        current = next_node
    llist.head = None
    llist.tail = None

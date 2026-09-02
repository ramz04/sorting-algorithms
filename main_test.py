import pytest

from main import Queue, matchmake

run_cases = [
    [("Ted", "join"), (["Ted"], "No match found")],
    [("Barney", "join"), (["Barney", "Ted"], "No match found")],
    [("Marshall", "join"), (["Marshall", "Barney", "Ted"], "No match found")],
    [("Lily", "join"), (["Lily", "Marshall"], "Ted matched Barney!")],
    [("Robin", "join"), (["Robin", "Lily", "Marshall"], "No match found")],
    [("Carl", "join"), (["Carl", "Robin"], "Marshall matched Lily!")],
    [("Carl", "leave"), (["Robin"], "No match found")],
    [("Robin", "leave"), ([], "No match found")],
]

submit_cases = [
    pytest.param(
        ("Ranjit", "join"),
        (["Ranjit"], "No match found"),
        marks=pytest.mark.submit,
    ),
    pytest.param(
        ("Ranjit", "leave"),
        ([], "No match found"),
        marks=pytest.mark.submit,
    ),
    pytest.param(
        ("Victoria", "join"),
        (["Victoria"], "No match found"),
        marks=pytest.mark.submit,
    ),
    pytest.param(
        ("Quinn", "join"),
        (["Quinn", "Victoria"], "No match found"),
        marks=pytest.mark.submit,
    ),
    pytest.param(
        ("Zoey", "join"),
        (["Zoey", "Quinn", "Victoria"], "No match found"),
        marks=pytest.mark.submit,
    ),
    pytest.param(
        ("Stella", "join"),
        (["Stella", "Zoey"], "Victoria matched Quinn!"),
        marks=pytest.mark.submit,
    ),
]

queue = Queue()


@pytest.mark.parametrize(("user", "expected_state"), run_cases + submit_cases)
def test_matchmake(user, expected_state):
    print("\n---------------------------------")
    print(f"Queue: {queue}")
    name = user[0]
    action = user[1]
    if action == "leave":
        print(f"{name} left the queue.")
    if action == "join":
        print(f"{name} joined the queue.")
    print(f"Expecting Queue: {expected_state[0]}")
    print(f"Expecting Return: {expected_state[1]}")
    try:
        result = matchmake(queue, user)
    except Exception as error:
        result = f"Error: {error}"
    print(f"Actual Queue: {queue}")
    print(f"Actual Return: {result}")
    assert result == expected_state[1]
    assert queue.items == expected_state[0]

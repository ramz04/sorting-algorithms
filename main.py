from queue import Queue


def matchmake(queue: Queue, user: tuple[str, str]) -> str:
    name, action = user

    if action == "leave" and name in queue.items:
        queue.search_and_remove(name)
    elif action == "join":
        queue.push(name)

    if queue.size() == 4:
        user1 = queue.pop()
        user2 = queue.pop()
        return f"{user1} matched {user2}!"
    elif queue.size() < 4:
        return "No match found"
    
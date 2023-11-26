def solution(todo_list, finished):
    return [todo for todo, check in zip(todo_list, finished) if not check]
from typing import Any

# Class Stack; methods(append, pop, list)
# Stack => push , pop , peek , is_empty,size


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def push(self, item: Any) -> None:
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            self.stack.pop()
            return
        raise Exception('Stack is empty')

    def peek(self) -> Any:
        if not self.is_empty():
            return self.stack[-1]
        raise Exception('Stack is empty')

    def size(self) -> int:
        return len(self.stack)
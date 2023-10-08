"""
Реализовать структуру Стек, которая имеет три метода:
1) метод добавления элемента в стек;
2) метод, который удаляет и возвращает элемент с вершины стека;
3) метод, который возвращает максимум в стеке или кидает 
исключение и возвращает ошибку, если стек пустой.
"""

class MaxStack:
    def __init__(self):
        self.stack = []
        self.stack_max = []

    def push(self, value):
        if not self.stack_max or value >= self.stack_max[-1]:
            self. stack_max.append(value)

        self.stack.append(value)

    def pop(self) -> int:
        tmp = self.stack[-1]

        if tmp == self.stack_max[-1]:
            self.stack_max.pop()

        self. stack.pop()
        return tmp

    def max(self):
        return self.stack_max[-1]

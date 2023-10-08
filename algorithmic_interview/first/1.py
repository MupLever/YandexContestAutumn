"""
Есть структура дерева.
Есть класс-обработчик, получающий дерево.
Есть k запросов суммы элементов на любом уровне дерева.
Нужно реализовать метод, возвращающий за константное время 
сумму на любом уровне дерева.
"""

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Handler:
    def __init__(self, root: TreeNode):
        self.root = root
        self.amounts_level = {}
        if self.root:
            self.dfs(self.root, 0)

    def sum(self, level: int) -> int:
        return self.amounts_level[level]

    def dfs(self, node: TreeNode, height: int) -> None:
        if height not in self.amounts_level:
            self.amounts_level[height] = 0
        self.amounts_level[height] += node.value

        height += 1

        if node.left:
            self.dfs(node.left, height)
        if node.right:
            self.dfs(node.right, height)
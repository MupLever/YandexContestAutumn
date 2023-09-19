class Tree:
    class Node:
        def __init__(self):
            self.count = 1
            self.children = {}

    def __init__(self):
        self.sum = 0
        self.root = self.Node()

    def add(self, array):
        current_node = self.root
        for el in array:
            if el in current_node.children:
                self.sum += current_node.children[el].count
                current_node.children[el].count += 1
            else:
                current_node.children[el] = self.Node()
            current_node = current_node.children[el]

    def print(self):
        self._dfs(self.root)

    def _dfs(self, node):
        for el in node.children:
            print(f"{el}")
            self._dfs(node.children[el])


tree = Tree()
# tree.add([1,2,3,4])
# tree.add([1,2,3,5])
# tree.add([3,3,3])
# tree.print()
number_of_arrays = int(input())

for _ in range(number_of_arrays):
    input()
    tree.add(input().split())

# tree.print()
print(tree.sum)

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def tree_vertex_splitting(root, tolerance):
    # Helper function to check if a node needs to be split
    def check_split(node):
        if len(node.children) >= tolerance:
            print("Splitting node:", node.value)
            # Split the node by creating new child nodes
            for i in range(len(node.children) // 2):
                new_child = Node(node.value + i + 1)
                new_child.children = node.children[i * 2:(i + 1) * 2]
                node.children[i] = new_child
            node.children = node.children[:len(node.children) // 2]

    check_split(root)
    for child in root.children:
        tree_vertex_splitting(child, tolerance)

# Example usage
root = Node(1)
root.children = [Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8), Node(9)]
tree_vertex_splitting(root, 3)

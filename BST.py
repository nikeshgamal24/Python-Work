class Node:
    def __init__(self, symbol, value, flag):
        self.symbol = symbol
        self.value = value
        self.flag = flag
        self.left = None
        self.right = None

def Enter_Symbol(root, symbol, value, flag):
    if not symbol[0].isalpha():
        print("illegal symbol")
        return root

    if len(symbol) > 6:
        symbol = symbol[:6]

    if not root:
        return Node(symbol, value, flag)

    if symbol < root.symbol:
        root.left = Enter_Symbol(root.left, symbol, value, flag)
    elif symbol > root.symbol:
        root.right = Enter_Symbol(root.right, symbol, value, flag)
    else:
        print("doubly defined")

    return root


def Search_Tree(root, symbol):
    if not root:
        print("undefined symbol")
        return None

    if symbol < root.symbol:
        return Search_Tree(root.left, symbol)
    elif symbol > root.symbol:
        return Search_Tree(root.right, symbol)
    else:
        print(root.symbol, root.value, root.flag)
        return root


def Print_Table(root):
    if not root:
        return

    Print_Table(root.left)
    print(root.symbol, root.value, root.flag)
    Print_Table(root.right)


symbols = [("ORANGE", "32", False), ("PEAR", "1C", True), ("PEACH1", "2A", False), ("ORANGE", "60", True), ("PEACHI", "OD", False), ("BANANA", "23", True), ("MANGO", "50", False), ("MELLON", "45", True), ("APPLE", "80", True), ("PEAR", "5A", True), ("EGGPLANT", "6B", False)]

root = None
for symbol, value, flag in symbols:
    root = Enter_Symbol(root, symbol, value, flag)

search_symbols = ["ORANG", "CARROT", "APPLE", "MANGO"]
for symbol in search_symbols:
    Search_Tree(root, symbol)

Print_Table(root)


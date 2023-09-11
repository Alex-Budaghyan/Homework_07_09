class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'value: {self.value}, left: {self.left}, right: {self.right} '

    def __repr__(self):
        lines = []
        if self.right:
            found = False
            for line in repr(self.right).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " ┌─" + line
                elif found:
                    line = " | " + line
                else:
                    line = "   " + line
                lines.append(line)
        lines.append(str(self.value))
        if self.left:
            found = False
            for line in repr(self.left).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " └─" + line
                elif found:
                    line = "   " + line
                else:
                    line = " | " + line
                lines.append(line)
        return "\n".join(lines)

    def __eq__(self, other):
        if not self and other:
            return True
        if (self and not other) or (not self and other):
            return False
        return self.value == other.value and self.left == other.left and self.right == other.right


class BinarySearchThree:
    def __init__(self):
        self.root = None

    def insert_value(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        if value < self.root.value:
            if self.root.left is None:
                self.root.left = new_node
            temp = BinarySearchThree()
            temp.root = self.root.left
            temp.insert_value(value)
        elif value > self.root.value:
            if self.root.right is None:
                self.root.right = new_node
            temp = BinarySearchThree()
            temp.root = self.root.right
            temp.insert_value(value)

    def search_value(self, value):
        if self.root is None:
            return False
        elif self.root.value == value:
            return True
        elif value < self.root.value:
            temp = BinarySearchThree()
            temp.root = self.root.left
            return temp.search_value(value)
        elif value > self.root.value:
            temp = BinarySearchThree()
            temp.root = self.root.right
            return temp.search_value(value)

    def in_order(self):
        result = []
        if self.root:
            if self.root.left:
                left_tree = BinarySearchThree()
                left_tree.root = self.root.left
                result.extend(left_tree.pre_order())
            result.append(self.root.value)
            if self.root.right:
                right_tree = BinarySearchThree()
                right_tree.root = self.root.right
                result.extend(right_tree.pre_order())
        return result

    def pre_order(self):
        result = []
        if self.root:
            result.append(self.root.value)
            if self.root.left:
                left_tree = BinarySearchThree()
                left_tree.root = self.root.left
                result.extend(left_tree.pre_order())
            if self.root.right:
                right_tree = BinarySearchThree()
                right_tree.root = self.root.right
                result.extend(right_tree.pre_order())
        return result

    def post_order(self):
        result = []
        if self.root:
            if self.root.left:
                left_tree = BinarySearchThree()
                left_tree.root = self.root.left
                result.extend(left_tree.pre_order())
            if self.root.right:
                right_tree = BinarySearchThree()
                right_tree.root = self.root.right
                result.extend(right_tree.pre_order())
            result.append(self.root.value)
        return result

    def __hash__(self):
        return hash(id(self.root))

    def __eq__(self, other):
        if self.root is None and other.root is None:
            return True
        elif (self.root is None and not other.root) or (not self.root and other.root is None):
            return False
        return self.root == other.root

    def __len__(self):
        return len(self.pre_order())

    def __repr__(self):
        return repr(self.root)


bts = BinarySearchThree()
bts.insert_value(20)
bts.insert_value(19)
bts.insert_value(21)
bts.insert_value(23)
bts.insert_value(15)
bts.insert_value(13)
bts.insert_value(18)
bts.insert_value(17)
# b = BinarySearchThree()
# # print(bts.__repr__())
# b.insert_value(20)
# b.insert_value(19)
# b.insert_value(21)
# b.insert_value(23)
# b.insert_value(15)
# b.insert_value(13)
# b.insert_value(18)
# b.insert_value(17)
# print(bts.search_value(14))
print(bts.__repr__())
# bts.in_order()
# print()
# print(bts.pre_order())
# print()
print(len(bts))

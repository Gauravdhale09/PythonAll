# Binary search

class BinarySearchNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:  #check if node already exists
            return
        if data < self.data:
            # add node to left
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchNode(data)
        else:
            # add node to right
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchNode(data)
    def inorder(self):
        inorder = []
        #visit left

        if self.left:
            inorder = inorder +  self.left.inorder()

        inorder.append(self.data)

        if self.right:
            inorder = inorder + self.right.inorder()
        return inorder
    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False


    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right.delete(val)
        else:
            if self.right is None and self.left is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
def build_tree(elements):
    print("Building tree:", elements)
    root = BinarySearchNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == '__main__':
    root = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("Inorder:",root.inorder())
    root.delete(4)

    print("Inorder:", root.inorder())
    root.delete(20)
    print("Inorder:",root.inorder())
    print(root)


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def height(root):
    max_node_count = get_max_node_count(root)
    return max_node_count - 1


def get_max_node_count(root):
    print(f"root = {root}")
    if root is None:
        print("None, return 0")
        return 0

    return max(get_max_node_count(root.left), get_max_node_count(root.right)) + 1


with open('input.txt', 'r') as input_file:
    length = input_file.readline()
    print(length)
    nodes = input_file.readline()
    print(nodes)

    tree = BinarySearchTree()
    t = int(length)

    arr = list(map(int, nodes.split()))

    for i in range(len(arr)):
        tree.create(arr[i])

    print(height(tree.root))

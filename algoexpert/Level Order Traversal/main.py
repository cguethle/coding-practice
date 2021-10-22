from queue import Queue


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
def levelOrder(root):
    children_to_explore = Queue()
    children_to_explore.put(root)

    output = []
    while not children_to_explore.empty():
        node = children_to_explore.get()
        if node:
            output.append(node.info)
            children_to_explore.put(node.left)
            children_to_explore.put(node.right)

    print(" ".join(map(str, output)))

# def levelOrder(root):
#     output = [str(root.info)]
#     output.extend(get_level_order(root))
#     print(" ".join(output))
#
#
# def get_level_order(node):
#     if node is None:
#         return []
#     output = []
#     if node.left:
#         output.append(str(node.left.info))
#     if node.right:
#         output.append(str(node.right.info))
#     output.extend(get_level_order(node.left))
#     output.extend(get_level_order(node.right))
#     return output


with open('input.txt', 'r') as input_file:
    length = input_file.readline()
    # print(length)
    nodes = input_file.readline()
    # print(nodes)

    tree = BinarySearchTree()
    t = int(length)

    arr = list(map(int, nodes.split()))

    for i in range(t):
        tree.create(arr[i])

    levelOrder(tree.root)

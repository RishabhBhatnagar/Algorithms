class Node():
    def __init__(self, data = "", frequency = 0):
        self.right_child = None
        self.left_child = None
        self.data = data
        self.frequency = frequency

import collections

string = input("Enter a string : ")
frequencies = dict(collections.Counter(string))
leaves = []
for i in frequencies:
    leaves.append(Node(i, frequencies[i]))
leaves = sorted(leaves, key = lambda x : x.frequency, reverse = False)
l = leaves.copy()

while leaves:
    try:
        leaf1 = leaves.pop(0)
        leaf2 = leaves.pop(0)
        parent = Node(leaf1.data+leaf2.data, leaf1.frequency+leaf2.frequency)
        parent.left_child = leaf1
        parent.right_child = leaf2
        leaves.append(parent)
        leaves = sorted(leaves, key = lambda x : x.frequency, reverse = False)
    except:
        root = leaf1

def inorder(root):
    if root:
        inorder(root.left_child)
        print(root.data)
        inorder(root.right_child)

frequencies = {}

def search(root, search_word, f_value):
    if root:
        if root.data == search_word:
            frequencies[search_word] = f_value
            return f_value
        else:
            if search_word in root.left_child.data:
                search(root.left_child, search_word, f_value+"0")
            else:
                search(root.right_child, search_word, f_value+"1")
    else:
        print("Doesn't exist in the tree")

for leaf in l:
    search(root, leaf.data, '')

print(frequencies)
string = ""
for i in l:
    string += frequencies[i.data]
print("final encoded string : ",string)

"""
OUTPUT:
Enter a string : malayalam
{'m': '111', 'a': '0', 'y': '110', 'l': '10'}
final encoded string :  110111100
"""

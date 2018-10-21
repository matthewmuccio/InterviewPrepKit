#!/usr/bin/env python3


""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def checkBST(root):
    lst = []
    def inorder(node):
        if node.data:
            if node.left:
                inorder(node.left)
            lst.append(node.data)
            if node.right:
                inorder(node.right)
        return lst
    inorder_lst = inorder(root)
    return sorted(list(set(inorder_lst))) == inorder_lst

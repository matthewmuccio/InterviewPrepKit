#!/usr/bin/env python3


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

def print_doubly_linked_list(node):
    nodes = []
    while node:
        nodes.append(str(node.data))
        node = node.next
    print(" ".join(nodes))

# Complete the sortedInsert function below.
def sortedInsert(head, data):
    node = DoublyLinkedListNode(data)
    if not head:
        return node
    elif data < head.data:
        node.next = head
        head.prev = node
        return node
    else:
        node = sortedInsert(head.next, data)
        head.next = node
        node.prev = head
        return head


if __name__ == "__main__":
    t = int(input())
    for t_itr in range(t):
        llist_count = int(input())
        llist = DoublyLinkedList()
        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)
        data = int(input())
        llist1 = sortedInsert(llist.head, data)
        print_doubly_linked_list(llist1)

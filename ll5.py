#!/usr/bin/env python3


# Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.
def has_cycle(head):
    curr = head
    i = 0
    while(i < 100):
        curr = head.next
        i += 1
        if not curr:
            return False
    return True

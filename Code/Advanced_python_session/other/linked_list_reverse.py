# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 15:09:52 2018

@author: debs_
"""
class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.value = data
        self.next = None
        
def reverse(l):
    if l is None:
        return None
    prev=None
    current = l
    fwd = l.next
    j = 1
    while (fwd is not None):
        current.next = prev
        prev = current
        current = fwd
        fwd = fwd.next
        j   += 1
    current.next = prev
    return current, j
def print_list(l):
    lstring = '[ '
    while (l.next is not None):
        lstring += str(l.value) + ', '
        l = l.next
    lstring += str(l.value) + ' ]'
    print(lstring)
def reverse(list):
    current = list
    previous = None
    
    while current is not None:
        previous, current.next, current = current, previous, current.next
        
    return previous
if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next = b
    b.next = c
    print_list(a)
    rev_a, len_a = reverse(a)
    print_list(rev_a)
    print(len_a)
        
        
    

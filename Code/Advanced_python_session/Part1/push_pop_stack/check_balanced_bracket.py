# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 16:08:09 2018

@author: debs_
"""

close_bracket = [')', '}', ']']
open_bracket  = ['(', '{', '[']
bracket_map = dict(zip(close_bracket, open_bracket))
def is_matched(expression):
    """
    create a stack, as you parse the string from left to right
    if you encounter an open bracket push it to the end of the stack
    if you encounter a closed bracket pop the end of the stack and match if the closed and open bracket match
    finally at the end if there are still items in the stack , brackets are not balanced.
    """
    check = []
    for i in expression:
        if i in open_bracket:
            check.append(i)
        elif i in close_bracket:
            if len(check) == 0:
                return False
            else:
                last_item = check.pop()
                if last_item != bracket_map[i]:
                    return False
    if len(check) > 0:
        return False
    else:
        return True

exprs = ['{[()]}','{[(])}',"\{\{[[(())]]\}\}"]
for a0 in range(len(exprs)):
    expression = exprs[a0]
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

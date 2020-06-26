#!/usr/bin/env python3

def add_one(a_list=[]):


<    """Demonstrate terrible, mutable defaults"""

a_list.append(1)
return a_list


print(add_one())
print(add_one())
print(add_one())

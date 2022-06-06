#!/usr/bin/python3

def add(a, b):
    len_a = len(a)
    len_b = len(b)

    if len_a == 0 and len_b == 0:
        return (0, 0)
    elif len_a == 0 and len_b == 1:
        return (b[0], 0)
    elif len_a == 1 and len_b == 0:
        return (a[0], 0)
    elif len_a == 1 and len_b == 1:
        return (a[0] + b[0], 0)
    elif len_a == 1 and len_b == 2:
        return (a[0] + b[0], b[1])
    elif len_a == 2 and len_b == 1:
        return (a[0] + b[0], a[1])
    else:
        return (a[0] + b[0], a[1] + b[1])

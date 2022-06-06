#!/usrbin/python3

def max_integer(my_list=[]):
    max = None

    for ele in my_list:
        if max is None or max < ele:
            max = ele
    return max

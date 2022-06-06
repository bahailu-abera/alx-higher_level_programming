#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    if not my_list:
        pass
    elif idx < 0 or len(my_list) <= idx:
        return my_list
    else:
        temp = []
        for index in range(len(my_list)):
            if index != idx:
                temp.append(my_list[index])
        return temp

#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not isinstance(my_list, list) or not isinstance(idx, int) or idx < 0:
        return my_list

    list_length = len(my_list)

    if idx >= list_length or list_length == 0:
        return my_list

    new_list = my_list[:idx] + my_list[idx+1:]
    return new_list

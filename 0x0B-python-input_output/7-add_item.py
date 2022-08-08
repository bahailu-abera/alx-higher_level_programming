#!/usr/bin/python3
""" Docs """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """ Adds all arguments to a python list, and then save them to a file """
    args = sys.argv
    args = args[1:]
    filename = "add_item.json"
    new_list = []
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []
    if my_list:
        my_list.extend(args)
        new_list = my_list
    else:
        new_list = args
    save_to_json_file(new_list, filename)


if __name__ == "__main__":
    main()

#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(args[0], args[1])

    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return None
    else:
        return result

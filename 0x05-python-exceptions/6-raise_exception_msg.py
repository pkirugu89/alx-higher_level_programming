#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        # raise a name exception with the provided message
        raise NameError(message)
    except NameError as e:
        # Re-raise the exception
        raise

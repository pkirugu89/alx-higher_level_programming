#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        # Handle division by 0
        result = None
    except Exception as e:
        # Handle other exceptions
        print(f'Exception: {e}')
        result = None
    finally:
        print("Inside result: {}".format(result))

    # Return the value of the division or None
    return result

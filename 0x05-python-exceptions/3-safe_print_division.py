#!//usr/bin/python3
def safe_print_division(a, b):
    try:
        answer = (int(a) / int(b))
    except ZeroDivisionError:
        answer = None
    finally:
        print("Inside result: {}".format(answer))
        return answer

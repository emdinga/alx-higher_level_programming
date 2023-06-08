#!/usr/bin/python3
if __name__ == "__main__":
    def add(a, b):
        from add_0 import add
        a = 1
        b = 2
        return add(a, b)
    print("{} + {} = {}".format(a, b, add(a, b)))

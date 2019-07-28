# example11.py
from plac import arg, call


def main(i: arg("This is an int", type=int),
         n: arg("This is a float", type=float),
         *rest: "Other arguments"):
    print(i, n, rest)


if __name__ == '__main__':
    call(main)

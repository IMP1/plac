# example10.py
from plac import arg, call


def main(operator: arg("The name of an operator", choices=['add', 'mul']),
         *numbers: arg("A number", type=float, metavar='n')):
    "A script to add and multiply numbers"
    if operator == 'mul':
        op = float.__mul__
        result = 1.0
    else:  # operator == 'add'
        op = float.__add__
        result = 0.0
    for n in numbers:
        result = op(result, n)
    return result


if __name__ == '__main__':
    print(call(main))

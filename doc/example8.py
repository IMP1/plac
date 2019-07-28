# example8.py
from plac import opt, call


def main(command: opt("SQL query"), dsn):
    if command:
        print('executing %s on %s' % (command, dsn))
        # ...


if __name__ == '__main__':
    call(main)

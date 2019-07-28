# example8_.py
from plac import opt, call


def main(dsn, command: opt("SQL query") = 'select * from table'):
    print('executing %r on %s' % (command, dsn))


if __name__ == '__main__':
    call(main)

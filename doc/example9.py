# example9.py
from plac import arg, flg, call


def main(verbose: flg('prints more info'),
         dsn: arg('connection string')):
    if verbose:
        print('connecting to %s' % dsn)
    # ...


if __name__ == '__main__':
    call(main)

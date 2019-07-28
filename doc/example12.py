# example12.py
from plac import call


def main(opt: ('some option', 'option'),
         *args: 'default arguments',
         **kw: 'keyword arguments'):
    if opt:
        yield 'opt=%s' % opt
    if args:
        yield 'args=%s' % str(args)
    if kw:
        yield 'kw=%s' % kw


if __name__ == '__main__':
    for output in call(main):
        print(output)

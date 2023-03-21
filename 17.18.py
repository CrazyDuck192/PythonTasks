from collections import Counter

def lower(func):

    def _lower(*args):
        args_lower = ''
        for arg in args:
            args_lower += arg.lower()
        y = func(args_lower)

        return y

    return _lower

@lower
def count(s):
    return Counter(s)

if __name__ == '__main__':
    s = 'abcdABCefgGFAB'
    g = 'qQQqqwerERwww'
    print(count(s, g))
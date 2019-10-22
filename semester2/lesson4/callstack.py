def foo():
    bar()
    biz()
    print("foo")


def bar():
    baz()
    print("bar")

def baz():
    print("baz")

def biz():
    print("biz")

foo()
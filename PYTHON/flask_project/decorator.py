def hello(func):
    def wrapper():
        print('hello')
        func()
        print('hellohello')

    return wrapper

@hello
def bye():
    print('byebye')

bye()
# hello()
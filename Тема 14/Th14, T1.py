from functools import wraps


def logger(func):
    @wraps(func)
    def wrap(*args):
        print(func.__name__ + ' called with ' + str([func(*args).__closure__[i].cell_contents for i in range(len(func(*args).__closure__))]) + '.')
    return wrap

        
@logger
def add(x, y):
    def add_1():
        return x + y
    return add_1

@logger
def square_all(*args):
    def square_all_1():
        return [arg ** 2 for arg in args]
    return square_all_1


if __name__ == '__main__':
    add(4, 5)
    print('')
    square_all(1, 2, 3)   



        



# def outer(message):
#     print('In the outer function')
#
#     def inner():
#         print('calling the inner function')
#         print(message)
#
#     return inner


# f = outer("Hello world")
# f()
# decorator
def decorator(original_func):

    print('In the decorator function\n')

    def wrapper():
        print(f'weapper executed before {original_func.__name__}()')

        if 10 > 5:
            print('yes it is true')

        return original_func()

    return wrapper


# non keyword arguments => f(1,2,3)
# keyword arguments => f(a=1,b=2,c=3)

def decorator_2(original_func):

    print('In the decorator_2 function\n')

    def wrapper(*args, **kwargs):
        print(f'weapper executed before {original_func.__name__}()')

        if 10 > 5:
            print('yes it is true')

        return original_func(*args, **kwargs)

    return wrapper


# @decorator
# def print_something():
#     print('print_something is being ran!')
#
#
# print_something()

@decorator_2
def print_something_more(arg1, arg2):
    print(f'printing argument_1 = {arg1} and argument_2 = {arg2}')


print_something_more(1, 2)
# using decorator 1 Way
# dec_fun = decorator(print_something)
# dec_fun()

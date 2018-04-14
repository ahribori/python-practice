def print_hello():
    print('hello')


def print_param(param):
    print(param)


def return_param(param):
    return param


def return_two_values():
    return 1, 2


print_hello()
print_param('hello, world!')
print(return_param('hi'))
(one, two) = return_two_values()
print(one)
print(two)
print(return_two_values())







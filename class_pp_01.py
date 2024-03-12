def add_profile(index, ix, iy, area):
    print(
        f'Adding profile {index} with moments of inertia Ix={ix} cm4, Iy={iy} cm4 and area {area} cm2')


# # invoking / calling the function ver 01
add_profile('MC014', 166.9, 23.6, 14.99)
# # invoking / calling the function ver 02
# add_profile(index='MC014', ix=166.9, iy=23.6, area=14.99)
# # which one is more clear and easier to handle ??
# print ("DEFAULT (optional) ARGUMENTS")
# # we can define default arguments in function definition
# print('1_line', 'Hello')
# print('2,line', 'World')

print('1_line', 'Hello', sep="", end=' ')
print('2_line', 'World', sep="")
print('1_line', 'Hello')
print('2_line', 'World')
#


def add_item(item_name, quantity=1):
    print(f'{quantity} units of {item_name} was added')


add_item('bread')
add_item('apples', 2)


def print_numbers_tuple(*numbers):  # * is for turple assignment
    print(numbers)


def print_numbers(*numbers):
    for n in numbers:
        print(n)


def summarize(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum


print_numbers_tuple(1, 2, 3)


def add_user(**user: dict) -> None:
    print(user)
    print(type(user))


def print_user(**user):
    for key, value in user.items():
        print(f' {key} = {value}')


add_user(id=1, name='abc', surname='def', age=25)
print_user(name='Alice', age=30, city='Wonderland')
var1 = 1
if (1 == 1):
    a = 1
print(a)
for i in [1, 2, 3]:
    b = 1
print(b)

user = []


def add_user(**user: dict) -> None:
    users.append(user)


def my_func():
    message = 'hrllp'
    print(message)


my_func()

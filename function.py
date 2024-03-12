def func1(*args):
    for i in args:
        print(i)


func1(20, 40, 60)
func1(80, 100)
'''-----------------------------'''


def calculation(a, b):
    # Your Code
    return a+b, a-b


res = calculation(40, 10)
print(res)
'''-----------------------------'''
def showEmployee(name, salary=9000):
    print("Name:", name, "salary:", salary)


showEmployee("Ben", 12000)
showEmployee("Jessa")
'''-----------------------------'''

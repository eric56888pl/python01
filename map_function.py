'''def dobuler(x):
    x *= 2
    return x'''


list_val = [1, 2, 3, 4, 5]
# answer = map(dobuler, list_val)
answer = map(lambda x: x*2, list_val)
print(list(answer))

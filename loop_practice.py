'''row = int(input('Enter a number: ')) 

for i in range(1, row + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')'''
row = int(input('Enter a number: '))

n = row
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print('')
'''Enter a number: 5
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5'''
'''--------------------------------'''
number = int(input('enter a number:'))
sum = 0
for i in range(1, number+1):

    sum = sum+i
print(sum)
'''--------------------------------'''
num = int(input('enter a number :'))
for i in range(1, 11):
    result = num*i
    print(result)
'''--------------------------------'''
numbers = [12, 75, 150, 180, 145, 525, 50]
for item in numbers:
    if item > 500:
        break
    elif item > 150:
        continue
    elif item % 5 == 0:
        print(item)
'''--------------------------------------'''
row = int(input('enter a number:'))
k = row+1
for i in range(1, row+1):
    k = k-1
    for j in range(k, 0, -1):

        print(j, end='')
    print('')

'''
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1'''
'''----------------------------------------'''
list1 = [10, 20, 30, 40, 50]
for x in range(50, 1, -10):
    print(x)
'''----------------------------------------'''
for i in range(-10, 0, 1):
    print(i)
'''----------------------------------------'''
for i in range(5):
    print(i)
print("Done!")
'''----------------------------------------'''
start = 25
end = 50
for num in range(start, end+1):
    for i in range(2, num):
        if num % i == 0:
            break
    else: 
        print(num)
'''----------------------------------------'''


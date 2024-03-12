def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'Fizzbuzz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    else:
        return num


while True:
    num = input('enter a number:')
    if num == 'q':
        break
    else:
        num = int(num)
        result = fizz_buzz(num)
        print(result)

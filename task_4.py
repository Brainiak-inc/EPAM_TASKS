def factorial_count(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial
n = int(input('Введите число:'))
print(factorial_count(n))
input()

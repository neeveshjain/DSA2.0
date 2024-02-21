def factorial(n):
    assert n >= 0 and int(n) == n, "The num is -ve or not an int"
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)

def fibbo(num):
    assert num >= 0 and int(num) == num, 'Fibonacci number cannot be negative or no integer.'
    if num == 0 or num == 1:
        return num
    else:
        return fibbo(num - 1) + fibbo(num - 2)
def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half = power(a, n // 2)
        return half * half
    else:
        return a * power(a, n - 1)

def fibonacci(n):
    if n < 0:
        raise ValueError("Cannot be a negative number")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1
 
    else:
        return fibonacci(n-1) + fibonacci(n-2)
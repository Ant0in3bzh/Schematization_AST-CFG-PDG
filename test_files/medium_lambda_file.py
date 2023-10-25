def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_list = [0, 1]
        while len(fib_list) < n:
            next_val = fib_list[-1] + fib_list[-2]
            fib_list.append(next_val)
        return fib_list


if __name__ == "__main__":
    print("Factorial of 5:", factorial(5))
    print("Fibonacci sequence of 10:", fibonacci(10))

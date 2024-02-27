# Example Python code for demonstration purposes

def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_sequence = [0, 1]
        for i in range(2, n + 1):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence[-1]

def main():
    num = int(input("Enter the number of Fibonacci numbers to generate: "))
    fib_numbers = [fibonacci(i) for i in range(num)]
    print("Generated Fibonacci numbers:", fib_numbers)

if __name__ == "__main__":
    main()

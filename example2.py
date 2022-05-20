# Example 2: Python code to be optimized

# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Function to print prime numbers up to a given limit
def print_prime_numbers(limit):
    primes = [num for num in range(2, limit + 1) if is_prime(num)]
    print("Prime numbers up to", limit, "are:", primes)

# Main function to demonstrate the usage of the above functions
def main():
    limit = int(input("Enter the limit: "))
    print_prime_numbers(limit)

if __name__ == "__main__":
    main()

# Example 1: Python code to be optimized

# Function to calculate the square of a number
def calculate_square(number):
    return number ** 2

# Function to print a message with the square of a number
def print_square_message(number):
    square = calculate_square(number)
    print(f"The square of {number} is: {square}")

# Main function to demonstrate the usage of the above functions
def main():
    number = int(input("Enter a number: "))
    print_square_message(number)

if __name__ == "__main__":
    main()

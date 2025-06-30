def print_diamond(size):
    for i in range(size):
        # Print leading spaces
        for j in range(size - i - 1):
            print(" ", end="")
        # Print asterisks
        for k in range(2 * i + 1):
            print("*", end="")
        print()

    for i in range(size - 2, -1, -1):
        # Print leading spaces
        for j in range(size - i - 1):
            print(" ", end="")
        # Print asterisks
        for k in range(2 * i + 1):
            print("*", end="")
        print()

# Example
if __name__ == "__main__":
    size = 5
    print_diamond(size)

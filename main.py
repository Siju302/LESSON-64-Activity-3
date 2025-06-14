number = int(input("Enter a number: "))

# Convert number to binary
binary = bin(number)[2:]

# Count 0s and 1s
zeros = binary.count("0")
ones = binary.count("1")

# Show results
print(f"\nBinary of {number} is: {binary}")
print(f"Number of 1s: {ones}")
print(f"Number of 0s: {zeros}")
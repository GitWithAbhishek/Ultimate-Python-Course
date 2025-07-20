import sys

# Get command line arguments
if len(sys.argv) != 3:
    print("Usage: python add.py <num1> <num2>")
    sys.exit(1)

# Convert arguments to integers
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

# Add numbers
result = num1 + num2

# Print result
print("Sum:", result)

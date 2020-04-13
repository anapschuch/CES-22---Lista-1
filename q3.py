def sum_to(n):
    """Returns the sum of all integer numbers up to and including n"""
    sum = n * (n + 1) / 2
    return int(sum)


n = int(input("Type a positive integer number: "))

# Print the result
print("The sum of the integer numbers from 1 up to ", n, ' is ', sum_to(n))

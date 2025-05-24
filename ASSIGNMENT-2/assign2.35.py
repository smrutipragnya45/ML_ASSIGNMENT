# Accept Variable Number of Arguments and Return Their Product
def product(*args):
    result = 1
    for num in args:
        result *= num
    return result

# Example usage:
print("Product:", product(2, 3, 4))
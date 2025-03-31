# Write a function to calculate the sum of all numbers in a list that are greater than a given number.

def sum_greater_than(numbers, n):
    # Filter numbers greater than n and calculate the sum
    return sum(num for num in numbers if num > n)

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7]
n = 5
print(sum_greater_than(numbers, n))

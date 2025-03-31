# Write a function to culculate the sum of elements in a list that are less than a given number.

def sum_less_than(numbers, n):
    # getting all numbers less than n
    return sum(num for num in numbers if num < n)

numbers = [1,2,3,4,5,6,7]
n = 5

 #call the function
print(sum_less_than(numbers, n))
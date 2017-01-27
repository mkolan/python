# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.

x = eval(input("Enter the number: "))

def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)


print(fact(x))

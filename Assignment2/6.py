'''Write a program to find the maximum of 2 numbers using normal
function and then using ternary operator and then illustrate the
same using lamdba function ?'''
x, y = input("Enter two values: ").split()
print("Maximum number is: ", max(x, y))

small_num = x if x > y else y
print(small_num)

ans = lambda x, y: x if x > y else y
print("maximum of two nos is:",ans(x, y))

'''Write a program to find the sum of the digits of the number recursively upto n iterations?

Input

Enter the number -139

Enter iterations - 2'''


def sum_of_digit(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digit(int(n / 10))


print("Enter number")
num = int(input())
print("Enter no.of iterations")
it = int(input())
ans = num
it = 2
for i in range(it):
    ans = sum_of_digit(ans)
    print(ans)

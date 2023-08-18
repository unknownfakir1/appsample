'''Write a program using loops and
closure to find the multipliers of 4 (4,8,12,16,....,40)?'''
# using loops
i = 1
lst = []
while i <= 10:
    lst.append(4 * i)
    i = i + 1
print(lst)

# using closure
listed = []


def outer(n):
    def multiply(i):
        return i * n

    return multiply


obj = outer(4)
for i in range(1, 11):
    listed.append(obj(i))
    print(obj(i))
print(listed)

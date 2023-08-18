'''Given an array of ints length n,
return an array with the elements "rotated left" so {1, 2, 3}
yields each iteration until {2, 3, 1} comes. Eg:

rotate_left1([5, 11, 9]) → [11, 9, 5]

rotate_left2([7, 0, 0]) → [0, 7, 0]'''


def rotate_left(arr, n, m):
    while (m > 0):
        tmp = arr[0]
        for j in range(n - 1):
            arr[j] = arr[j + 1]
        arr[n - 1] = tmp
        m = m - 1


print("Enter length of array")
n = int(input())
print("Enter number of iterations")
m = int(input())
array = []
print("Enter elements")
for i in range(n):
    ele = int(input())
    array.append(ele)
print("Array before rotation: ", array)
rotate_left(array, n, m)
print("Array after rotation: ", array)

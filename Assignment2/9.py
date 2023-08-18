'''Write a function that will take one list as input and
return three different types of list as illustrated in the output.
In object2, you can append a list containing triplet of a number
 but object 3 should be evaluated based on the elements present in the object2
 (Note:You have to take care of both the space and time complexities as well)

Input:

object1 = [[1,1,1],[2,2,2],[3,3,3]]

Output:

object1 = [[1,1,1],[2,2,2],[3,3,3]]

object2 = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]

object3 = [[1,1,1],[2,4,2],[3,9,3],[4,16,4]]'''
import copy

object1 = []
print("Enter first triplet")
a, b, c = input().split()
lst1 = []
lst1.append(int(a))
lst1.append(int(b))
lst1.append(int(c))
object1.append(lst1)
lst2 = []

print("Enter second triplet")
a, b, c = input().split()
lst2 = []
lst2.append(int(a))
lst2.append(int(b))
lst2.append(int(c))
object1.append(lst2)
lent=len(lst2)

print("Enter third triplet")
a, b, c = input().split()
lst3 = []
lst3.append(int(a))
lst3.append(int(b))
lst3.append(int(c))
object1.append(lst3)
print("Object1: ", object1)

lent = len(object1)
tmp = object1[lent - 1][lent - 1]
nw_lst = []
nw_lst.append(tmp + 1)
nw_lst.append(tmp + 1)
nw_lst.append(tmp + 1)
object2 = []
object2.append(lst1)
object2.append(lst2)
object2.append(lst3)
object2.append(nw_lst)
print("Object2: ", object2)

object3 = []
object3 = copy.copy(object2)  # shallow
# object3 = copy.deepcopy(object2) #deep
# print (type((object3[1][1])))

new_len=len(object3)
for i in range(new_len):
    object3[i][1] = object3[i][0] * object3[i][lent-1]
print("Object 1 after operation: ",object3)
print("Object 2 after operation: ",object2)

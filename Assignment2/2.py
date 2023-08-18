'''Write a function to reverse words of the sentence?(Check the output carefully)

Input:

“I love programming.”

Output:

“.programming love I”'''
def reverse(str):
    st = ""
    for i in str:
        st = i + st
    return st


print("Enter string")
string = input()
print("The original string is: ", string)
print("The reversed string is: ", reverse(string))

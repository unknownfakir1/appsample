'''Write a function that accepts a sequence of
 whitespace separated words as input and prints the words
 after removing all duplicate words and sorting them alphanumerically?
(Both with and without second list)'''

print("Enter the words")
word = input()
word_split = word.split(' ')
#print(type(word_split))
print(word_split)

#without using second list
word_split=sorted(set(word_split))
print(word_split)

#Using second list
lst = []
for i in word_split:
    if i not in lst:
        lst.append(i)
lst.sort()
print(lst)

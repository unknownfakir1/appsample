'''Write a password generator program of 8 characters that contains
at least one uppercase, one lower case, one digit and one special
symbol? (Every new password should be different than the previously generated one).'''
import random
import array

len = 8
dig = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lower_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v'
              'w', 'x', 'y', 'z']
upper_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V'
    , 'W', 'X', 'Y', 'Z']
special_char = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                '*', '(', ')', '<']
lst = dig + upper_char + lower_char + special_char
rand_dig = random.choice(dig)
rand_upper = random.choice(upper_char)
rand_lower = random.choice(lower_char)
rand_special = random.choice(special_char)
tmp = rand_upper + rand_lower + rand_special + rand_dig

for i in range(len - 4):
    tmp = tmp + random.choice(lst)
    tmp_lst = array.array('u', tmp)
    # print(tmp_lst)
    random.shuffle(tmp_lst)

pwd = ""
for i in tmp_lst:
    pwd = pwd + i
print(pwd)

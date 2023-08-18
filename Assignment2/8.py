'''Write a program to illustrate
the use of default, keyword, optional
and variable length args (*args and **kwargs)?'''
str = ''


def welcome_msg(*args):
    global str
    for arg in args:
        str += arg
    print(str)


def cal_si(principal, yr, roi=5):
    si = (principal * yr * roi) / 100
    return si


def invoice_of_recipient(**recipient):
    print("The recipient {} has Rs {}".format(recipient["fname"], amt))


welcome_msg("Welcome ", "to ", "New York Bank")

print("Enter your principal amount and duration")
principal, yr = input().split()
principal = int(principal)
yr = int(yr)

print("Enter name,middle name,surname")
name, middle_name, surname = input().split(" ")
amt = cal_si(principal, yr)

invoice_of_recipient(fname=name, mname=middle_name, lname=surname)

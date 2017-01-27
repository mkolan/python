# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# var = input("Enter your sentence")
# def number_le_di(x):
#     dict = {'LETTERS':0,'DIGITS':0}
#     for i in x:
#         if i.isalpha():
#             dict['LETTERS'] += 1
#         elif i.isdigit():
#             dict['DIGITS'] += 1
#     print("LETTERS", dict['LETTERS'])
#     print("DIGITS",dict['DIGITS'])
#
# number_le_di(var)


##################################################################################################
# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

# var = input("Enter your sentence")
# def cal_up_low(x):
#     dict = {'UPPER CASE':0,'LOWER CASE':0}
#     for i in x:
#         if i.islower():
#             dict['LOWER CASE'] += 1
#         elif i.isupper():
#             dict['UPPER CASE'] += 1
#     print("UPPER CASE",dict['UPPER CASE'])
#     print("LOWER CASE",dict['LOWER CASE'])
#
# cal_up_low(var)

########################################################################################################

# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

# def compute():
#     try:
#         x = int(eval(input("Enter your number")))
#         n1 = int("%s" %x)
#         n2 = int("%s%s" %(x,x))
#         n3 = int("%s%s%s" %(x,x,x))
#         n4 = int("%s%s%s%s" %(x,x,x,x))
#         print(x)
#         print(type(x))
#         print(n1+n2+n3+n4)
#     except:
#         print("Input is not an int")
# compute()

#######################################################################################################
# Question:
# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9


def square_odd():
    x = eval(input("enter values seperated by comma\'s"))
    nums = [i for i in x.split(',') if i%2 != 0]
    print(','.join(nums))

square_odd()
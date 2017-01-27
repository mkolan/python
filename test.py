# import math
#
# def vol(rad):
#     return (4/3)*math.pi*(rad) ** 3
#
# print(vol(3))

######

# def ran_check(num,low,high):
#     if num in range(low,high+1):
#         print("This number is in range",num)
#     else:
#         print("Not in range")
#
# ran_check(8,1,7)

#######
# s = "abcbcbbghb ASDHGTFTGH"
#
# def low_up(str):
#     lower = 0
#     upper = 0
#     for letter in str:
#         if letter.islower():
#             lower += 1
#         else:
#             upper += 1
#     print("No.of upper: ",upper)
#     print("Lower: ", lower)
#
# low_up(s)

#####

# l = [1,1,1,1,2,3,4,5,2,3,4,5,6,6,7,8,9,34,7]
#
# def uniq_list(list):
#     uniq = set(list)
#     print(uniq)
#
# uniq_list(l)


######
# l = [1,2,-4, 20,2]
#
# def mul_num(list):
#     mul = list[0]
#     for i in list:
#         mul *= i
#     return mul
# print(mul_num(l))


######polindrome

# def poli(str):
#     if str == str[::-1]:
#         return  True
#     else:
#         return False
# print(poli("dangnaddfhdbjhf"))


########

# dict = {"upper" : 0 , "lower": 0, 'digit': 0}
#
# def dict1(s):
#     for char in s:
#         if char.isupper():
#             dict['upper'] +=1
#         elif char.islower():
#             dict['lower'] += 1
#         elif char.isdigit():
#             dict['digit'] += 1
#         else:
#             pass
#
# dict1("FHJJHjhggHGhvjk4353536337123jbJHJB")
# print("lower", dict['lower'])
# print("upper", dict['upper'])
# print("digit", dict['digit'])

###### Uniq list
# def uniq1(l):
#     op = []
#     for i in l:
#         if i not in op:
#             op.append(i)
#     return op
# print(uniq1([1,2,3,3,4,4,5,5,56]))

#####
import string

# def is_pangram(str):
#     alphabets = str.ascii_lowercase
#     total = set(alphabets)
#     return total
#
# print(is_pangram("abcdefghijklmnopqrstuvwxyz"))


# class Dog():
#     tyres = 4
#     def __init__(self,breed, name):
#         self.my_breed = breed
#         self.name = name
#
# sam = Dog('lab','sammy')
# danny = Dog('german shepherdyyy', 'danny')
# print(sam.my_breed,sam.name)
# print(sam.tyres, danny.name)
# print(danny.my_breed)



# def highest(x):
#     l = [2, 3, 4, 57,5,6,6,7,8]
#     l1 = set(l)
#     return l1[x]
#
# print(highest(5))


def apple(username,password):
    print(username,password)

apple(username="userjhbmdhfbdfmhbfdmnmfdbfdjbfdfmjjdfbcdbvdchnvdchdfhname",password = 'mypasswrd')


# def madhu(a,b):
#     print(a,b)
#
#
# madhu(1,2)
# madhu(a=11, b= 21)

# def madhu1(a,b,c=2):
#     print(a,b,c)
#
#
# madhu1(1,2,c=4)


## *args
# def madhu2(*args):
#     for i in args:
#         print(i)
#
# a = (1,2,3)
#
# madhu2(a)

## **kwargs

# def madhu3(**kwargs):
#     for i,j in kwargs.items():
#         print(i,j)
#
#
# madhu3(me="you",we="just")


## sum args
# def me(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
#
# me(1,2,3)
# me(3,3,45)
#

## ex:

def me(*args):
    for i in args:
        print(i)


me(1,23,3)










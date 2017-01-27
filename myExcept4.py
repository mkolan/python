try:
    num = eval(input("enter a number"))
    print("The number is", num)
except NameError as ex:
    print ("The Exception is : ", ex)
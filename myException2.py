try:
    num1, num2, num3 = (input("Enter two numbers seperated by commasssss:"))
    result = num1/num2
    print("The result is",result, num3)
except ZeroDivisionError:
    print("Zero division")
except SyntaxError:
    print("Pbm with syntax")
except:
    print("wrong input")
else:
    print("No exception")
finally:
    print("From finally")


# num1, num2 = eval("10","8")
# print(num1,num2)

# x = 1
# print(eval('x+1'))

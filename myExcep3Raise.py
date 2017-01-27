def ageValidate(age):
    if age < 0:
        raise ValueError("Only positives allowed")
    elif age % 2 == 0:
        print("Age is even")
    else:
        print ("Age is odd")
try:
    age = input("Enter your age: ")
    ageValidate(age)
except ValueError:
    print ("Only positive integers please")
except:
    print ("Some thing is wrooong")
finally:
    print ("From finally block")
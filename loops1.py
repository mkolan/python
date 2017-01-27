# For
# list1 = [1,2,3,4]
# for i in list1:
#     print(i)

#    Range)
# for i in range(1,11,2):  ## range(1,10) also a case
#     print(i)


# While
# count = 0
# while count < 10:
#     count += 1
#     print(count)
#


  # Break
  # if condition is true control goes out of the loop
count = 0
while count < 10:
    count += 1
    if count == 5:
        break
    print("Inside loop", count)
print("outside loop")


## Continue -- it breaks the current iteration and goes to the end of the loop body
## If condition is true breaks the inner most loop


# count = 0
# while count < 10:
#     count += 1
#     if count == 5:
#         continue
#     print(count)
# print("outside loop")
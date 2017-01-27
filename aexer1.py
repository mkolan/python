#######Finding common records from 2 files#####
# File open and write into it
# f1 = open("madhu1.txt",'w')
# f2 = open("madhu2.txt",'w')
#
# f1.write("123\n124\n125\n126\n127\n122\n128\n129\231\n")
# f2.write("123\n1254\n125\n127\n126\n125\n124\n122\n")
#
def file_intersection():
    with open('madhu1.txt','r') as f1:
        with open('madhu2.txt','r') as f2:
            inter = set(f1).intersection(set(f2))
            with open('madhu3.txt','w') as f3:
                for line in inter:
                    f3.write(line)



####'
# f1 = open('madhu1.txt','r')
# f2 = open('madhu2.txt','r')
# f3 = open('madhu4.txt', 'w')
#
# for line1 in f1:
#     for line2 in f2:
#         if line1 == line2:
#             f3.write("%s\n"%(line1))
# f3.close()
# f2.close()
# f1.close()

######Finding xth highest number from a list
# def highest(x):
#     l = [2,3,1,6,4,4,6,4,1,4,565]
#     l1 = list(set(l))
#     l1.sort()
#     return l1[-x]
#
# print(highest(2))


##### Reverse records in a file #####
# def reverse_records():
#     f0 = open('madhu6.txt','w')
#     with open('madhu2.txt','r') as f:
#         lines =  f.readlines()
#         lines.reverse()
#         for line in lines:
#             f0.write(line)
#     f.close()
#     f0.close()
# reverse_records()

#####JSON objects insertion into a postgreSQL

#### Recursive factorial

# def fact(n):
#
#      if n == 0:
#          return 1
#      else:
#          return n * fact(n-1)
#
# print(fact(6))


##### fibonacci Recursive

# def fibonacci(n):
#     list = []
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#     list.append(n)
#     print(list)
#
# print(fibonacci(9))
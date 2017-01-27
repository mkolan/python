f = open('madhuFile1.txt', 'w')
f.write("This is linexhhvhvh 1 \n")
f.write("This is linexhgsdjdsjbdsjksdkjbkjdskj 2 \n")
f.write("This is linexhhvhvhdsfsdhgdshgvhgdsvdsvsvsvshvhsdjhsd 3 \n")

f.close()

# f = open("madhuFile1.txt", 'w') ##If the file is already present, It will open the file and empty the content!
# f.close()
#
# f = open('madhuFile1.txt', 'r') ##opening the file in read only mode
# f.close()

# f = open('madhuFile234.txt', 'r')
# f.close()
# f = open('madhuFile1.txt', 'r')
# print(f.readlines())
# f.close()

f = open("madhuFile1.txt", 'a')  ##appends at the end of the file
f.write("appending line \n")
f.close()

## looping in files
f = open("madhuFile1.txt", 'r')
for line in f:
    print (line)
f.close()

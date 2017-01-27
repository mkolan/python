def sum(start, end):
    result = 0
    for i in range(start, end+1):
        result += i
    print(result)

sum(1,10)



def sum1(start, end):
    result = 0
    for i in range(start, end+1):
        result += i
        return result

s = sum1(1,11)
print(s)


## Returns None

def test():
    i = 0
print(test())

## local  global
g = 10
def func():
    l = 100
    print(g)
    print(l)
func()




##

def me(a,b,c):
    print(a,b,c)

me(1,2,3)


##
def me1(a,b,c = 1):
    print(a,b,c)
    return a,b

mex= me1(1,4, c=6)
print(mex)

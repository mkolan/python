try:
    f = open('somefie.txt')
    print(f.read())
    f.close()
except ZeroDivisionError:
    print('dummy....')
except IOError:
    print ("no file")



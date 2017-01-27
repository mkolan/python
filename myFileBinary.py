import pickle

f = open('myBinary.dat', 'wb')
pickle.dump(1,f)   ## Dumps the contents into binary file using dump methos from pickle module
pickle.dump([1,2,3,4], f)
pickle.dump([1,2,3,4,'me','you'], f)
f.close()



f = open('myBinary.dat', 'rb')
print(pickle.load(f))
print(pickle.load(f))
print(pickle.load(f))
f.close()
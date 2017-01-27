class Person:
    def __init__(self, name):
        self.name = name


    def whoami(self):
        return "you're " + self.name



p1 = Person('madhu')
print(p1.name)
print (p1.whoami())
p1.name = "meeeee"
print (p1.name)
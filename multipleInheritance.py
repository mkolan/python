class A:
    def a(self):
        print("From a")


class B:

    def b(self):
        print("From b")


class Me(A,B):
    def c(self):
        print("From My class")


obj = Me()
print(obj.a())
print(obj.b())
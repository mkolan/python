class A:
    def __init__(self):
        self.x = 1

    def m1(self):
        print("From parent")


class B(A):
    def __init__(self):
        self.y = 1


    def m1(self):
        print("m1 from child")


obj = B()
obj.m1()

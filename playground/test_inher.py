class B:
    def __init__(self):
        print("B")

class C:
    def __init__(self):
        print("C")

class A(B, C):
    def __init__(self):
        super(A, self).__init__()
        print("A")

a = A()
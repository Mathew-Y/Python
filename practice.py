class A:
    def __init__(self, id):
        self.x = id

class B:
    def __init__(self, id):
        self.x = A(id + 1)

class C:
    def __init__(self, id):
        self.x = B(id + 1)

x = C(10)

print(type(x.x.x))
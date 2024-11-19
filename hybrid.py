class p:
    def add(self):
        print("This is added")
class q(p):
    def div(self):
        print("This is added")

class r(q):
    def mul(self):
        print("This is added")


class s(r):
    def min(self):
        print("This is added")
class t(r):
    def sum(self):
        print("This is added")

obj=s()
obj.add
obj.min

obj.mul
obj.div

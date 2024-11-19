class papa:
    def add(self,a,b):
        print(a+b)
    def minus(self,a,b):
        print(a-b)
class son(papa):
    def mul(self ,a,b):
        print(a*b)
obj=son()
obj.add(13,13)
obj.mul(13,13)
obj.minus(13,13)                    
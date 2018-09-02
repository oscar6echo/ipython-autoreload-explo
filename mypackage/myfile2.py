
class MyClass2:

    def __init__(self, a=10):
        self.a = a
        self.b = 11

    def power(self, p):
        print('compute power '+str(p))
        return self.a**p

    # def poweradd(self, p, i=1):
    #     print('compute power '+str(p))
    #     return self.a**p+i

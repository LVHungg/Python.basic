class myClass():
    def menthod1(self):
        print('Đây là lớp cơ sở')

class myClass1():
    def menthod01(self):
        print('Đây là lớp cơ sở')

class childClass(myClass1, myClass):
    def menthod2(self):
        print('Đây là lớp con')

c2 = childClass()
c2.menthod01()
c2.menthod2()



        
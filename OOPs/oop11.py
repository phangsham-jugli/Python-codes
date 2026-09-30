#Multiple inheritance
class A:
    def state_1(self):
        print("State 1 ,class A")
    def state_2(self):
        print("State 2 ,class B")

class B:
    def state_3(self):
        print("State 3 ,class B")
    def state_4(self):
        print("State 4,class B")

class C(A,B):
    def state_5(self):
        print("State 5 ,class C")
    def state_6(self):
        print("State 6,class C")

c=C()
c.state_1()
c.state_2()
c.state_3()
c.state_4()
c.state_5()
c.state_6()
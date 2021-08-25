# import time
#
# class oldphone:
#     __brand = ""
#     phonenumber = ""
#     def setCall(self,brand):
#         self.__brand = brand
#     def getCall(self):
#         return self.__brand
#
#     def call(self, phone):
#         print(self.phonenumber,"正在给",phone,"打电话...")
#         for i in range(5):
#             print('.', end="")
#             time.sleep(0.5)
#
# class newphone(oldphone):
#     brand = ""
#     def call(self,number):
#         super().call(number)
#         print("\n语音拨号中")
#         for i in range(5):
#             print(".",end="")
#             time.sleep(0.5)
#
#     def intro(self,name):
#         print("\n",name,"的手机很好用！")
#
#
# p = newphone()
# p.brand = "HUAWEI"
# p.phonenumber = "13578956897"
# p.call("18468678521")
# p.intro("HUAWEI")

class Cook:
    __name = None
    __age = None

    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def setAge(self,age):
        if age <= 0 or age >100:
            print("error")
        else:
            self.__age = age
    def getAge(self):
        return self.__age

    def zhengfan(self):
        print("蒸干饭")

class Cook1(Cook):
    def chaocai(self):
        print("炒个菜")

class Cook2(Cook1):
    def zhengfan(self):
        super().zhengfan()
        print("蒸饭")
    def chaocai(self):
        super(Cook2, self).chaocai()
        print("炒菜")

    def intro(self):
        print(self.getName(),"是一个厨师，他今年",self.getAge(),"岁了。")

c = Cook2()
c.setAge(24)
c.setName("小明")
c.intro()

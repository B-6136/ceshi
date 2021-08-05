'''
实现输入10个数字，并打印10个数的求和结果
'''
print('和：',1+2+3+4+5+6+7+8+9+10)
print('-----------------------')
print('-----------------------')
'''
从键盘依次输入10个数，最后打印最从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数
'''
num1 = input("输入第一个数字：")
num2 = input("输入第二个数字：")
num3 = input("输入第三个数字：")
num4 = input("输入第四个数字：")
num5 = input("输入第五个数字：")
num6 = input("输入第六个数字：")
num7 = input("输入第七个数字：")
num8 = input("输入第八个数字：")
num9 = input("输入第九个数字：")
num10 = input("输入第十个数字：")
sum = float(num1) + float(num2) + float(num3) + float(num4) + float(num5) + float(num6) + float(num7) + float(num8) + float(num9) + float(num10)
print('数字相加结果为： {10}'.format(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10,sum))

print('-----------------------')
print('-----------------------')

'''
从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形（结果判断：等腰，等边，直角，普通，不能形成三角形。）
'''
while True:
    a = input("输入第一条边：")
    b = input("输入第二条边：")
    c = input("输入第三条边：")
    a = int(a)
    b = int(b)
    c = int(c)
    if a + b > c or a + c > b or b + c > a or a>0 and b>0 and c>0 :
        print('可以构成三角形')
        if a == b == c:
            print('该三角形是等边三角形')
        if a == b or a == c or b == c:
            print('该三角形是等腰三角形')
        if a^2 + b^2 == c^2 or a^2 + c^2 == b^2 or b^2 + c^2 == a^2 :
            print('该三角形是直角三角形')
    else:
        print('无法构成三角形')
        jixu = input("是否继续(y/n):")
        if jixu == 'y':
            continue
        elif jixu == 'n':
            break





print('-----------------------')
print('-----------------------')
'''
# 有以下两个数，使用+，-号实现两个数的调换。
# A=56
# B=78
# '''

a = 56
b = 78
a = a + b # a=134 b=78
b = a - b # b=134-78=56 a=134
a = a - b
print("a的值为：",a)
print("b的值为：",b)


print('-----------------------')
print('-----------------------')
'''
实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
'''

count = 0
d = {"user1":"0001","user2":"0002","user3":"0003","user4":"0004","user5":"0005"}
while count <= 3:
    name = input("输入用户名：")
    if name in d:
        password = input("输入密码：")
        if d[name] == password:
            print("登录系统")
            break
        else:
            count = count + 1
            print("密码错误")
        continue
    else:
        print("用户名错误")
        continue
else:
    print("连续输入三次密码错误，账户锁定")

'''
while计算1-100和
'''
sum = 0
start = 1
while start <=100:
    sum = sum + start
    start = start + 1 # start += 1
print(sum)

'''
青蛙爬井
'''

d = 1
h = 0
while h < 20:
    h = h + 3
    if h < 20:
        h = h - 2
    else:
        break
    d += 1
print("第",d,"天出来")

'''
从键盘输入6课成绩，统计总分、平均分、最高分、最低分
'''
score1 = input("输入第一课成绩：")
score2 = input("输入第二课成绩：")
score3 = input("输入第三课成绩：")
score4 = input("输入第四课成绩：")
score5 = input("输入第五课成绩：")
score6 = input("输入第六课成绩：")
score1 = int(score1)
score2 = int(score2)
score3 = int(score3)
score4 = int(score4)
score5 = int(score5)
score6 = int(score6)
sum = score1 + score2 + score3 + score4 + score5 + score6
print('总成绩为',sum,'分')
avg =(score1 + score2 + score3 + score4 + score5 + score6)/ 6
print('平均分',avg,'分')
print('最高分',max(score1,score2,score3,score4,score5,score6))
print('最低分',min(score1,score2,score3,score4,score5,score6))

'''
图形打印
'''
for h in range(1,8,1):
    for f in range(0,8-h):
        print(end=" ")
    for s in range(8-h,8):
        print("*",end=" ")
    print(" ")

'''
99乘法表
'''
i = 1
while i <= 9:
    j=1
    while j<=i:
        print(j,'x',i,'=',(i*j),"\t",end="")
        j = j+1
    print()
    i = i + 1

'''
倒叙乘法表
'''
i = 9
while i >= 1:
    j = 1
    while j <= i:
        print(j,'x',i,'=',(i*j),"\t",end="")
        j = j+1
    print()
    i = i - 1
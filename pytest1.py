import  math
import django
print("123")
# list = /['abcd', 786, 2.23, 'runoob', 70.2]
# tinylist = [123, 'runoob']
#
# print(list)  # 输出完整列表
# print(list[0])  # 输出列表第一个元素
# print(list[1:3])  # 从第二个开始输出到第三个元素
# print(list[2:])  # 输出从第三个元素开始的所有元素
# print(tinylist * 2)  # 输出两次列表
# print(list + tinylist)  # 连接列表
# tup=(1,2,3,4)
# str='abc123'
# print(str)
# print(str[0])
# print(str*2)
# list=['123','sad','f3qw',"ee",1323]
# print(list)
# print(list[1])
# print(list[2:3])
# list[1]=2
# print(list[1])
# set={'tom','jerry','jimmy','ken','tom','tom'}
# print(set)
# # set[1]=1
# # print(set)
# print(list[:])
#
# a =list
#
# print(a is list)
# b=2
# c=3
# c **= b
# print(c)
# print(c.bit_length())
# print(len(list))
# for i in range(10,22,3):
#     print(i)
# list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
# for x in list:
#     print (x, end=" ")


def ChangeInt( a ):
    a = 10
    # return a

b = 2
ChangeInt(b)
print( "\n",ChangeInt(b))
def chang(list):
    list.append([1,2,3,4])
    print("函数内取值：",list)
    return
mylist=[12,13,14]
chang(mylist)
print("函数外取值：",mylist)
def priintof(name ='da',age=20):
    print(name)
    print(age)
    return
priintof()
# if _name_ == '_main_':
s='helloKitty'
print(str(s))
print(repr(s))
print('{0}和{1}'.format('hr','gh'))
print('π近似值{}'.format(math.pi))
print('π近似值{0:.2f}'.format(math.pi))

list=12.332323
n=len(str(list))
print("----------------------------",n)
def infor():
    for i in range (10000):
        i=i+1
        print(i)


infor()



def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
divide(3,1)
divide(3,1)
class newclass:
    i=22
    def h(s):
        return 'sdsf'
d=newclass()
print("类属性：",d.i)
print("类的方法：",d.h())
class comd:
    def __init__(se,t1,t2):
        se.r=t1
        se.i=t2
o=comd (10,11)
print(o.i,o.r)

num = int(input("请输入一个数字: "))

# 初始化变量 sum
sum = 0
# 指数

n = len(str(num))



# 检测
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

# 输出结果
if num == sum:
    print(num, "是阿姆斯特朗数")
else:
    print(num, "不是阿姆斯特朗数")



for i in range(1,10000,1):
    temp=i
    sum=0
    temp1=temp
    list=[]
    for y in range(1,10000,1):
        if temp1 < 1:
            # print(temp1)
            break
        temp =temp1% 10
        list.append(temp)
        temp1//=10
        # print("list为",list)
    n=list.__len__()
    # print(n)

    for t in range(0,list.__len__(),1):
        sum +=list[t]**n
        # print("----合计为------",sum)

    if sum==i:
        print("-------------------阿姆斯特朗数为--------：",i)

for i in range(0,1000,1):
    temp = i
    n=len(str(temp))
    sum =0
    while temp >0:
        di=temp % 10
        sum+=di**n
        temp //=10
    if sum == i:
        print("阿姆斯特朗数为--------：", i)


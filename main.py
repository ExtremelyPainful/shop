# str1 = "sdoianjcbascbnawqda"
#
# print(str1[9])
#
# countNum = str1.count("1")
# print(countNum)

# a = input()
# if int(a) < 0:
#     print("负数")
# elif int(a)>=0 or int(a) <= 50:
#     print("小于50或者大于0")
# elif int(a) >=50 or int(a)<= 100:
#     print("大于50或者小于或等于100")
# else:
#     print("请输入小于100的数")
a = []
b = 0
for i in range(1,100):
    if (i % 3 == 0):
        b+=i
        a.append(i)
print(a)
print(b)


for i in range(1,10):
    for j in range(1,i+1):
        print(i,"*",j,"=",i*j,end="\t")
    print(" ")

def countNUmber(a,b,c,d):

    return a+b+c+d
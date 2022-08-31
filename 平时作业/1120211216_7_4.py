import random
acc=0
for i in range(5):
	print("第{}关".format(i+1))
	num1=random.randint(0,100)
	num2=random.randint(0,100)
	print("两个随机数分别是{}、{}".format(num1,num2))
	sum=int(input("请输入两数之和："))
	if sum==num1+num2:
		acc=acc+1
tureAcc=acc/5
if tureAcc>=0.8:
	print("闯关成功")
else:
	print("闯关失败")

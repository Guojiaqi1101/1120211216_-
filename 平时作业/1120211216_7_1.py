num=int(input("请输入一个整数："))
n=num
multi=1
while num>=1:
	multi=multi*num
	num=num-1
print("1~{}的乘积为：{}".format(n,multi))

num=int(input("请输入一个整数："))
if num<2:
	print("{}不是素数".format(num))
else:
	for i in range(2,num):
		if num%i==0:
			print("{}不是素数".format(num))
			break
		else:
			print("{}是素数".format(num))


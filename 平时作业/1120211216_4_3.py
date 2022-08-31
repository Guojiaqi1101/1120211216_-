num=int(input("输入一个整数："))
i=1
s=num
while i<20:
	s=s*num
	i=i+1
L=len(str(s))
print("%d的20次幂的值为%d，位数为%d"%(num,s,L))

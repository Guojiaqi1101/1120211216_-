a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
detla=b*b-4*a*c
if detla<0:
	print("没有实数根")
elif detla==0:
	x=(-b+detla)/(2*a)
	print("有一个实数根：{}".format(x))
else:
	x1=(-b+detla)/(2*a)
	x2=(-b-detla)/(2*a)
	print("有两个实数根，分别是：{}，{}".format(x1,x2))

num=int(input("请输入三位整数："))
gw=num%10
sw=num//10%10
bw=num//100%10
multi=gw**3+sw**3+bw**3
print("{}的水仙花数：{}".format(num,multi))

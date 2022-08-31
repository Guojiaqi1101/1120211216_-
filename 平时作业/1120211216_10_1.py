path1="score.txt"
f1=open(path1,"r",encoding='utf-8')
num=0
table={}
counts={}
for line1 in f1.readlines():
	newline1=line1.rstrip()
	newwords1=newline1.split(" ")
	table[num]=newwords1
	num+=1
for i in table:
	score=table[i]
	grade=score[3]
	counts[grade]=counts.get(grade,0)+1

items=list(counts.items())
j=1
while j<=2:
	grade,count=items[j]
	print("{}年级共有{}人".format(grade,count))
	j=j+1
f1.close
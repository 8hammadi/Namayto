def to_number(s):
	l=s.split("_")
	for i in range(len(l)):
		if len(l[i])==1:
			l[i]="0"+l[i]
	r="".join(l)
	if r[0]=="0":
		r=r[1:]
	return r

def to__(r):
	if len(r)%2==1:
		r='0'+r
	l=[r[i:i+2] for i in range(0,len(r),2)]
	for i in range(len(l)):
		if l[i][0]=="0":
			l[i]=l[i][1:]
	return  "_".join(l)

s="1_2_41_3"

import re
handle=open("romeo.txt")
all_sum=0
for line in handle:
	line=line.rstrip()
	lists=[int(i) for i in re.findall('[0-9]+',line)]
	all_sum=all_sum+sum(lists)
print(all_sum)
	
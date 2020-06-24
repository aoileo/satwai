n=int(input())
temp = input().split(' ')
days = 0
for i in temp:
	if int(i) < 0:
		days +=1
print(days)
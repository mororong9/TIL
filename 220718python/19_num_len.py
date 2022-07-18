num=123456
cnt=0
while num!=0:
    num//=num #몫을 구하는 방법 = num=num//10
    cnt+=1
print(cnt)

num=123456
print( len(str(num))) #str인 경우 


import math
num=123456
print(int(math.log(num, 10))+1)
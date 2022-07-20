num=123
print(int(str(num)[::-1]))

result=0
while num:
    result*=10
    result+=num%10
    num//=10
print(result)

#alt  방향키 
#컨 알트 동시에 쓰기
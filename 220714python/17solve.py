word='babaaa'
result=''
for char in word:
    num=ord(char)#알파벳을 숫자로
    num=num-32
    result+=(chr(num))#다시 숫자를 알파벳으로 
print(result)

for char in word:
    print(char(ord(char)-32),end='')
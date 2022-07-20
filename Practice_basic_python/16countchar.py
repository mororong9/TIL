word=input()
num=0
for i in word:
    if i=='a':
        num+=1
    elif i=='e':
        num+=1
    elif i=='i':
        num+=1
    elif i=='o':
        num+=1
    elif i=='u':
        num+=1
print(f'{num}')

'''for i in word:
    if word.isalpha('a')==True:
        num+=1
print(f'{num}')'''
'''문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
모음 : a, e, i, o, u 
count() 사용 금지'''
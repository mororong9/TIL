word='happy!'
num=0
print('select the way in 1, 2, 3')
select= int(input())
if select ==1:
    for i in enumerate(word):
        num+=1
    print(num)
    
elif select==2:
    while num<len(word):
        num+=1
    print(f'{num}')
else:
    for i in word:
        num+=1
    print(f'{num}')   

'''
문자열 word의 길이를 출력하는 코드를 1) while문 2) for문(문자열 그대로) 3) for문(index)으로 각각 작성하시오.

**len() 함수 사용 금지**


### Input

python
word = 'happy!'


### Output
6
'''
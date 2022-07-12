print('1부터 더할 숫자를 입력')
num=int(input())
print('방법을 선택')
select=int(input())
sum=0
i=0
if select==1:
    while i<num+1:
        sum+=i
        i+=1
    print(f'{sum}')
else:
    for i in range(num+1):
        sum+=i
    print(f'{sum}')
'''
> 1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

**sum() 함수 사용 금지**
> 

### Input

```python
n = 10
```

### Output
'''
print('1부터 곱할 숫자를 입력')
num=int(input())
print('방법을 선택')
select=int(input())
mul=1
i=1
if select==1:
    while i<num+1:
        mul*=i
        i+=1
    print(f'{mul}')
else:
    for i in range(1,num+1):
        mul*=i
    print(f'{mul}')


'''
> 1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.
> 

### Input

```python
n = 5
```

### Output
120

'''
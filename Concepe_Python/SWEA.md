### SWEA 1288

중복제거(set), set의 길이가  10이되면 종료

```python
T=int(input())
for test_case in range(1,T+1)
	T=int(input())
    numbers=set()# set add untill ten
    while len(numbers)<10: #add set in numbers
        for n in str(N):
            numbers.add(n)
        if len(numbers)==10:
            break
        N+=N1
    print(f'#{test_case}{N}')

```


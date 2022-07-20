numbers = [0, 20, 100]
max=0
for i in numbers:
    if max<i:
        max=i
print(max)

'''
아래의 테스트 케이스로도 확인 해보세요.

```python
numbers = [0, 20, 100, 50, -60, 50, 100] # 100
numbers = [0, 1, 0] # 1
numbers = [-10, -100, -30] # -10 
```

### Output
'''
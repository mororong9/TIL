from unittest import result


students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
def sort(studnets):
    result=0
    for i in students:
        if '이영희'==i:
            result+=1
    return result
print(sort(students))
'''
# 문제 09. 득표수 구하기

# 문제

> 주어진 리스트가 반장 선거 투표 결과일 때 이영희의 총 득표수를 출력하시오.
> 

### Input

```python
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
```

### Output

```
4
```
'''
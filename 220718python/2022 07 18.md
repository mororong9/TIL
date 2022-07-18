2022 07 18

### 딕셔너리 메모

result[char]=result[char]+1 #딕셔너리 값 1 올리기



### 디버깅

control+shift +d=디버깅



### syntax error(문법에러)

- 결과는 실행되지 않음

- EOL(end of line)

- EOF(End of Fille)

- Invalid syntax

- assign to literal: 리터럴: 고정된 값을 대표하는 용어, 



### 예외

- ZeroDivisionError

- NameError: 선언되지 않은 변수 사용

- keyError:키가 없어서 발생되는 에러 

- ModulNotFoundError:존재하지 않는 모듈을 import 하는 경우 



### 예외처리

- try /except 문

```python
numbers=input('enter num')
try:
    print(100/int(number))
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다") #작은 단위를 위에 올림 (위에서부터 처리되기때문)
except Exception:
    print("오류")
```

- raise


a,b=map(int, input().split())
result=a*2**b
print(result)
'''

정수 2개(a, b)를 입력받아 a를 2**b배 곱한 값으로 출력해보자.
0 <= a <= 10, 0 <= b <= 10

예시
a = 2
b = 10
print(a << b)  #210 = 1024 가 출력된다.

참고
예를 들어 1 3 이 입력되면 1을 23(8)배 하여 출력한다.'''
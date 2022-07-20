T = int(input())
result=1
for test_case in range(1, T + 2):
        test_case*=result
        
        print(result,end=' ')
        result=result*2
        

'''
1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.

주어질 숫자는 30을 넘지 않는다.

입력
8
input.txt
출력
1 2 4 8 16 32 64 128 256
'''
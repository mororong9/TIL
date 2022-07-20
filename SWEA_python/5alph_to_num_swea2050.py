import sys
sys.stdin=open('2050_input.txt','r')

# T = input()
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in T:
#     result=int(test_case)
#     print(int(result), end=' ')

k = list(input())
for i in range(len(k)):
    print(ord(k[i])-64, end=' ')

''''

문자열의 최대 길이는 200이다.


[입력]

알파벳으로 이루어진 문자열이 주어진다.


[출력]

각 알파벳을 숫자로 변환한 결과값을 빈 칸을 두고 출력한다.
 

입력
ABCDEFGHIJKLMNOPQRSTUVWXYZ
input.txt
출력
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26'''
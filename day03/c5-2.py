#p.293 재귀함수 , 재귀란 자기 자신을 호출하는것
# 1] 팩토리얼
def factorial1(n):
    output = 1
    for i in range(1 , n+1):
        output *= i
    return output
factorial1(2) # 2! -> 1 ~ 2 -> 1 * 2
factorial1(3) # 3! -> 1 ~ 3 -> 1 * 2 * 3
# 만약에 n이 3이면 range( 1, 4 ) 반복하므로 
# i는 1일때 output = output * 1
# i는 2일때 output = output * 2
# i는 3일때 output = output * 3
# 1 * 2 * 3 => 3!
# 2]  팩토리얼 재귀
def factoriall2(n):
    # 무한 재귀 방지
    if n == 0:
        return 1
    else: # 재귀함수
        return n * factoriall2(n-1)

factoriall2(2)
factoriall2(3)
# 만약에 n이 3이면 n == 0 false
    # return n * factorial2( 2 )                                    return 3 * 2 * 1 * 1
        # n이 2이면 n == 0 false                                return 2 * 1 * 1
            # n이 1이면 n == 0 false
                # return n * factorial2(0)              return 1 * 1
                    # n이 0이면 n == 0 true         return 1 
# 함수 호출 1개당 리턴 1번 => 함수 3번 호출 / 리턴 3번

# 구구단 반복문
for 단 in range( 2 , 10 , 1): # 단 : 2부터 9까지 1씩 증가
    for 곱 in range(1 , 10 , 1): # 곱 : 1부터 9까지 1씩 증가
        print( 단*곱)
# 3단/4곱 까지의 반복문 순서도 작성 

# 구구단 재귀
def 구구단(단=2 , 곱=1) :
    if 단 > 9: # 재귀 끝
        return
    if 곱 > 9: # 단마다 곱하기 9까지 했으면 단 올리기
        구구단( 단+1 , 1 )
        return
    print(단 * 곱)
    구구단(단 , 곱 + 1) # 곱 올리기
구구단( )

# p.315 1번
seatmin = 2
maxseatmin = 10
allmin = 100
memo = {}

def const_seat(남은사람, 직전인원):
    key = str([남은사람, 직전인원])
    # 종료 조건
    if key in memo:
        return memo[key]
    if 남은사람 < 0:
        return 0
    if 남은사람 == 0:
        return 1
    else :
        output = 0
        for i in range(직전인원, maxseatmin + 1):
            output += const_seat(남은사람 - i , i)
        memo[key] = output
        return output

print(const_seat(allmin, seatmin))
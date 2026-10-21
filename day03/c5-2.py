#p.293 재귀함수 , 재귀란 자기 자신을 호출하는것
# 1] 팩토리얼
def factorial1(n):
    output = 1
    for i in range(1 , n+1):
        output *= i
    return output
factorial1(2) # 2! -> 1 ~ 2 -> 1 * 2
factorial1(3) # 3! -> 1 ~ 3 -> 1 * 2 * 3




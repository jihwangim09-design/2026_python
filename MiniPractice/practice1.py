import numpy as np

# 1] CSV 파일 로드 (헤더 제외, 콤마 구분)
#    [0] ID  [1] 기준년월  [2] 대여건수  [3] 반납건수
data1 = np.genfromtxt('./MiniPractice/ddareungi_1-6.csv',
                      delimiter=',', skip_header=1, encoding='utf-8-sig')
data2 = np.genfromtxt('./MiniPractice/ddareungi_7-12.csv',
                      delimiter=',', skip_header=1, encoding='utf-8-sig')
print(f"상반기: {data1.shape}, 하반기: {data2.shape}")    # (16403, 4) (16567, 4)


# 2] 병합 : 위아래로 붙이기 → 1~12월  (DAY07 n-03 vstack)
data = np.vstack([data1, data2])
print(f"1~12월 데이터 형태: {data.shape}")               # (32970, 4)

# 3] 대여소별 12개월 합계
#    [0] ID  [1] 대여합계  [2] 반납합계
ids = np.unique(data[:, 0])                # 중복 없는 대여소번호 (오름차순)
rows = []
for i in ids:
    m = data[:, 0] == i                    # 이 대여소의 행만 True  (DAY07 n-03)
    rows.append([i, np.sum(data[m, 2]), np.sum(data[m, 3])])    # (DAY07 n-04)

대여소 = np.array(rows)
print(f"대여소별 데이터 형태: {대여소.shape}")          # (2812, 3)

# 4] 대여소 이름표 로드 (문자열 : DAY06 n-01 dtype)
#    [0] ID  [1] 이름   → station 과 같은 행 순서 (둘 다 ID 오름차순)

names = np.genfromtxt('./MiniPractice/ddareungi_names.csv',
                      delimiter=',', skip_header=1, encoding='utf-8-sig', dtype=str)
print(f"이름표 형태: {names.shape}")                     # (2812, 2)
print(대여소[:3])
print(names[:3, 1])




# step1
대여 = 대여소[:,1]
최다대여소 = np.max(대여)
최소대여소 = np.min(대여)
print(f"1년 평균 대여수: {np.mean(대여):,.1f}")
print(f"1년 최대 대여수: {최다대여소:,.1f} 대여소명: {names[np.argmax(대여) , 1 ]}" )
print(f"1년 최소 대여수: {최소대여소} 대여소명: {names[np.argmin(대여) , 1 ]}" )
반납 = 대여소[:,2]
print(f"1년 평균 반납수: {np.mean(반납):,.1f}")


# step2
n = len(대여소)
print(f"전체 대여소 개수: {n}")
대여정렬 = np.sort(대여)
반납정렬 = np.sort(반납)
상위10 = 대여정렬[int(n * 0.9)]
하위10 = 반납정렬[int(n * 0.1)]
print("대여 상위 10% 기준: " , 상위10)
print("반납 하위 10% 기준: " , 하위10)
그룹 = (대여 >= 상위10) | (반납 <= 하위10)
그룹수 = 대여소[그룹]
print("관리가 필요한 대여소: " , 그룹수.shape[0] , "곳")

# step3
불균형지수 = 대여 / 반납
최악 = np.argmax(불균형지수)

print("대여 반납이 가장 불균형한 대여소: " , names[최악 , 1])
print(f"불균형 지수: {불균형지수[최악]:,.1f} 배")


# [Step 4] 복합 위험군 : (불균형 지수 >= 1.2) & (대여건수 >= 중앙값)
위험군조건 = (불균형지수 >= 1.2) & (대여 >= np.median(대여))     
위험군 = 대여소[위험군조건]
print(f"대여건수 중앙값: {np.median(대여):,.0f}건")
print(f"복합 위험 대여소: {위험군.shape[0]}곳")
print(f"전체 대비 비율: {위험군.shape[0] / 대여소.shape[0] * 100:.1f}%")


# [Step 5] 순유출(대여 - 반납)을 0~1로 정규화 → 0.9 이상 = 재배치 최우선 대여소
순유출  = 대여 - 반납                                             
정규화 = (순유출 - np.min(순유출)) / (np.max(순유출) - np.min(순유출))      
조건 = 정규화 >= 0.9
결과  = 대여소[조건]
print(f"재배치 최우선 대여소: {결과.shape[0]}곳")

정렬 = np.argsort(순유출[조건])[::-1]       # 순유출 많은 순 
print(결과[정렬])                         # [ID, 대여, 반납]
print(names[조건, 1][정렬])              # 대여소 이름
print(순유출[조건][정렬])                   # 순유출 대수
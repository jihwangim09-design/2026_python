# httpx 란? 외부 api 통신하는 라이브러리 , API연동 / SPRING API
# 설치1 : pip install httpx
# httpx 라이브러리에는 .json() 타입변환 가능 하지만 xml 변환 지원하지 않는다
# xmltodict 란? xml 파싱 라이브러리
# 설치2 : pip install xmltodict
import httpx
import pandas as pd


# 0] 
service_key = "7540ef37d4d62e8aa1ccaf9c61bc9095638232be0930450a4a0d128c78e9e7d6"

# 1] 공공데이터에 json 형식의 자료 요청
def test1() :
    # "https://api.odcloud.kr/api/15052602/v1/uddi:855807e2-fe8a-4e47-8a5a-ce1894e410d7_201909031553?page=1&perPage=10&serviceKey=7540ef37d4d62e8aa1ccaf9c61bc9095638232be0930450a4a0d128c78e9e7d6"
    # 2] 신청한 API의 주소 및 파라미터 분석 , PAGE 현재 페이지 , perPAGE= 페이지당자료수 , servicekey
    url = "https://api.odcloud.kr/api/15052602/v1/uddi:855807e2-fe8a-4e47-8a5a-ce1894e410d7_201909031553"
    url += "?page=1"
    url += "&perPage=147"
    url += f"&serviceKey={service_key}"
    # 3] httpx 이용하여 통신하기
    # httpx.HTTP메소드명(통신할주소) , 통신 결과 반환
    response = httpx.get(url)
    print(response) # <Response [200 OK]> 성공했다는뜻
    # 4] 응답 결과 JSON 변환 , .json()
    response_json = response.json() # print( response_json )
    # 5] 판다스에 저장하기 , import pandas as pd
    df = pd.DataFrame( response_json['data']) # { "currentCount" : 10 , "data" : [실질자료]}
    df.info()



test1()

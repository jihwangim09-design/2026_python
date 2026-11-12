# [1] 라우터 : 특정 도메인(주소) 묶어주는 역할
from fastapi import APIRouter
router = APIRouter( prefix="/api" )

# [2] 서비스 객체 불러오기 (./Practice_day16/Service.py)
from Service import insurance_service

# 1) 예측 : 본문(JSON) -> dict 로 받아서 예측 결과 + 성능 지표 반환
@router.post("/predict")
async def predict( data : dict ):
    return insurance_service.predict( data )

# http://127.0.0.1:8080/api/predict 에 POST
# { "age": 30, "sex": "male", "bmi": 32.0, "children": 1, "smoker": "yes", "region": "southeast" }

# 2) 모델 정보 : 성능 지표 + 3개 모델 비교표
@router.get("/metrics")
async def metrics():
    return insurance_service.info()

# http://127.0.0.1:8080/api/metrics

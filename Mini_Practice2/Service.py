# 비지니스 로직 == 머신러닝 모델 예측
# 서버 시작 시 저장된 모델(.pkl)을 한 번만 불러오고, 요청마다 재학습 없이 예측만 수행한다.
import joblib
import pandas as pd

class InsuranceService :
    # 생성자 : 모델과 성능 지표 로드
    def __init__(self):
        self.model = joblib.load( './Mini_Practice2/insurance_model.pkl' )
        self.metrics = joblib.load( './Mini_Practice2/insurance_metrics.pkl' )

    def predict( self, data ):
        # 1. 입력 딕셔너리 -> 데이터프레임 (모델 입력 규격)
        df = pd.DataFrame( [data] )

        # 2. 학습 때와 동일하게 파생변수 생성 (빠뜨리면 컬럼 없음 에러)
        df['obese_smoker'] = 0
        df['obese_smoker'] = df['obese_smoker'].mask( ( df['bmi'] >= 30 ) & ( df['smoker'] == 'yes' ), 1 )

        # 3. 학습 때와 같은 컬럼 순서로 맞추기
        df = df[ ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'obese_smoker'] ]

        # 4. 예측
        pred = self.model.predict( df )

        # 5. 예측 결과 + 모델 성능 지표 반환
        return {
            'prediction' : round( float( pred[0] ), 2 ),         # 예측 보험료($)
            'obese_smoker' : int( df['obese_smoker'][0] ),       # 비만+흡연 위험군 여부 (1/0)
            'r2' : self.metrics['r2'],                           # 테스트 R2 (필수 지표)
            'model_name' : self.metrics['model_name'],           # 선택된 모델
            'best_params' : self.metrics['best_params']          # 최적 하이퍼파라미터
        }

    def info( self ):
        # 모델 성능 지표 전체 (비교표 포함)
        return self.metrics

##############################################################################
# 서비스 객체 생성
insurance_service = InsuranceService()

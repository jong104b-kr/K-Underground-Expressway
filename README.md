# K-Underground-Expressway
(Ministry Of Land, Infrastructure and Transport) 초장대 K-지하고속도로 인프라 안전 및 효율향상 기술개발

# 프로젝트 개요
## 목표
- 간단히 말하면 **​무엇을 만들고 싶은가​**?  
- 주요 사용 사례(예: 이미지 분류, 챗봇 등)와 기대 효과를 적어 주세요.

## 팀
- 담당자 이메일 / GitHub 핸들 (예: @alice, @bob)  
- 기여 가이드: `CONTRIBUTING.md` 참고

## 버전
- 현재 버전: v0.1.0  

---

## 데이터
### 데이터 소스
- **​공개 데이터셋​**: `torchvision` → CIFAR‑10, ImageNet 등  
- **​사내 데이터​**: `data/raw/` 폴더에 저장 (접근 권한은 별도 안내)

### 데이터 포맷
| 파일명 | 형식 | 설명 |
|--------|------|------|
| `train.csv` | CSV | 학습 샘플 |
| `test.csv`  | CSV | 테스트 샘플 |
| `labels.json`| JSON | 라벨 매핑 |

### 전처리 파이프라인
```python
# src/preprocess.py
def load_data(path: str) -> torch.utils.data.Dataset:
    # 구현은 필요 시 추가
    pass

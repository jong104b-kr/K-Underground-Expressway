---
name: Pull Request
about: PR 작성 시 반드시 채워 주세요.
title: "[Feature] "   # 혹은 "[Bug] ", "[Data] " 등
labels: 
  - status/needs-review
  - status/blocker?   # 필요 시
assignees: 
---

## 변경 내용 요약
- 핵심 변경 사항을 한 줄에 요약 (예: "ResNet‑50에 BatchNorm 추가")

## 관련 이슈
- 이 PR이 해결하는 이슈 번호: #123

## 테스트 결과
- 모든 테스트가 통과했나요? (`pytest` 결과 포함)  
- 새로 추가된 `torchmetrics` 검증 로그는?

## 체크리스트
- [ ] `pytest` 로 로컬 테스트 실행 (`pytest --cov`)
- [ ] Docker 이미지 빌드 성공 (`docker build -t ... .`)
- [ ] 코드 포맷 (black) 적용 (`black .`)
- [ ] 문서 업데이트 (`docs/` 폴더)

## 리뷰어에게 남길 코멘트
- 특별히 주의해 주길 바라는 부분
- 성능 개선 전후 비교 (가능하면 표)

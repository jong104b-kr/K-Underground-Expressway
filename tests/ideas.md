# PC 구조물 누수성능 연구 공정표 웹페이지 디자인 아이디어

## 연구 과제 개요
- **과제명**: 수직구 구조물 연결부 누수차단용 PC 구조물 제작 및 누수성능 검토
- **연구 방향**: 수직구 굴착 시 구조물 침하방지 선단부 구조물 적용성 검토 + 지하수 누수차단용 PC구조물 제작 및 연결부 누수성능 검토
- **핵심 마일스톤**: ⓐ시제품 제작, ⓑ연결부 및 누수성능 실증시험, ⓒ전시회, ⓓ보고서

---

<response>
<text>
## 디자인 아이디어 A: 엔지니어링 블루프린트 스타일 (Engineering Blueprint)

**Design Movement**: 산업 기술 도면(Blueprint) + 현대 대시보드 하이브리드

**Core Principles**:
1. 기술 문서의 정밀함을 시각적 언어로 표현
2. 데이터 계층 구조를 명확한 그리드 시스템으로 구현
3. 진행률과 마일스톤을 직관적인 타임라인으로 표현
4. 전문성과 가독성의 균형

**Color Philosophy**:
- 주색: 딥 네이비 (#0D1B2A) — 기술 신뢰감
- 강조색: 시안 블루 (#00B4D8) — 수직구·수자원 연상
- 보조색: 앰버 (#F4A261) — 경고/주의 마일스톤
- 배경: 오프화이트 (#F8F9FA) — 도면지 느낌

**Layout Paradigm**:
- 좌측 고정 사이드바 (네비게이션: 월간/주간/일일 전환)
- 메인 영역: 간트 차트 + 카드형 마일스톤
- 비대칭 그리드 (사이드바 20% + 메인 80%)

**Signature Elements**:
1. 도면 격자 배경 패턴 (미세 점선 그리드)
2. 진행 단계별 색상 코딩 배지
3. 연결선으로 이어진 타임라인 노드

**Interaction Philosophy**:
- 탭 전환으로 일일/주간/월간 공정표 전환
- 마일스톤 카드 호버 시 세부 정보 팝오버
- 간트 차트 바 클릭 시 상세 설명 확장

**Animation**:
- 페이지 로드 시 타임라인 바가 좌→우로 슬라이드인 (300ms ease-out)
- 카드 호버 시 subtle 상승 효과 (translateY -4px, 200ms)
- 진행률 바 카운트업 애니메이션

**Typography System**:
- 헤딩: Noto Sans KR Bold (700) — 한국어 기술 문서 최적화
- 본문: Noto Sans KR Regular (400)
- 수치/코드: JetBrains Mono — 기술적 느낌 강조
</text>
<probability>0.08</probability>
</response>

<response>
<text>
## 디자인 아이디어 B: 콘크리트 & 스틸 인더스트리얼 (Industrial Concrete)

**Design Movement**: 브루탈리즘(Brutalism) + 현대 미니멀리즘 하이브리드

**Core Principles**:
1. 재료의 물성(콘크리트, 철근)을 디자인 언어로 전환
2. 강한 타이포그래피 대비로 정보 계층 표현
3. 여백을 통한 집중도 극대화
4. 데이터 시각화를 주인공으로

**Color Philosophy**:
- 주색: 콘크리트 그레이 (#6B7280) — 재료 연상
- 강조색: 철근 오렌지 (#EA580C) — 구조 강조
- 배경: 순백 (#FFFFFF) + 연회색 섹션 (#F3F4F6)
- 텍스트: 차콜 (#111827)

**Layout Paradigm**:
- 풀와이드 섹션 기반 스크롤 내러티브
- 헤더 고정 + 섹션별 앵커 네비게이션
- 카드 그리드 (마일스톤 4개 병렬 배치)

**Signature Elements**:
1. 굵은 섹션 구분선 (4px 오렌지 액센트 라인)
2. 숫자 카운터 (대형 타이포그래피로 진행률 표시)
3. 수직 타임라인 (좌측 고정 진행 인디케이터)

**Interaction Philosophy**:
- 스크롤 기반 섹션 전환
- 필터 버튼으로 공정 카테고리 토글
- 차트 데이터 포인트 클릭 시 상세 모달

**Animation**:
- 스크롤 진입 시 요소 페이드인 (intersection observer)
- 진행률 바 fill 애니메이션 (스크롤 트리거)
- 숫자 카운트업 효과

**Typography System**:
- 헤딩: Noto Serif KR Bold — 권위감
- 서브헤딩: Noto Sans KR SemiBold
- 본문: Noto Sans KR Regular
</text>
<probability>0.07</probability>
</response>

<response>
<text>
## 디자인 아이디어 C: 테크 대시보드 (Tech Dashboard) ← 선택

**Design Movement**: 현대 SaaS 대시보드 + 한국 기술 보고서 하이브리드

**Core Principles**:
1. 정보 밀도와 가독성의 최적 균형
2. 인터랙티브 데이터 시각화 우선
3. 전문성을 유지하면서도 접근성 높은 UI
4. 모바일 반응형 우선 설계

**Color Philosophy**:
- 주색: 슬레이트 블루 (#1E3A5F) — 기술 신뢰감, 지하수 연상
- 강조색: 에메랄드 그린 (#059669) — 성공/완료 상태
- 경고색: 앰버 (#D97706) — 진행중 상태
- 위험색: 레드 (#DC2626) — 지연/주의 상태
- 배경: 라이트 슬레이트 (#F1F5F9)

**Layout Paradigm**:
- 상단 고정 헤더 (프로젝트 개요 + 전체 진행률)
- 탭 기반 뷰 전환 (개요/월간/주간/일일/마일스톤)
- 카드 그리드 + 전체폭 차트 혼합

**Signature Elements**:
1. 간트 차트 (Recharts 기반 인터랙티브)
2. 마일스톤 타임라인 (수직 진행 인디케이터)
3. KPI 카드 (핵심 지표 요약)

**Interaction Philosophy**:
- 탭 전환으로 공정표 뷰 변경
- 차트 호버 시 툴팁으로 세부 정보
- 마일스톤 클릭 시 상세 정보 확장
- 인쇄/저장 버튼

**Animation**:
- 탭 전환 시 슬라이드 페이드 (200ms ease-out)
- 카드 로드 시 스태거 애니메이션 (50ms 간격)
- 진행률 바 카운트업

**Typography System**:
- 헤딩: Noto Sans KR Bold (700)
- 본문: Noto Sans KR Regular (400)
- 수치: Roboto Mono — 데이터 가독성
</text>
<probability>0.09</probability>
</response>

---

## 선택된 디자인: C (테크 대시보드)

테크 대시보드 스타일을 채택합니다. 슬레이트 블루 기반의 전문적인 색상 체계와 인터랙티브 간트 차트, 탭 기반 공정표 뷰 전환을 통해 연구 데이터를 직관적으로 탐색할 수 있는 대시보드를 구현합니다.

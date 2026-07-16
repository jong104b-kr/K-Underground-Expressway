import numpy as np
from sklearn.linear_model import RANSACRegressor, LinearRegression
from sklearn.decomposition import PCA

# 가정: mvs_points 는 (N, 3) 크기의 Nx3 NumPy 배열 (X, Y, Z)
# mvs_points = ... (MVS 결과 로드)

# ---------------------------------------------------------
# 1. RANSAC 을 이용한 바닥면 (Floor Plane) 추정
# ---------------------------------------------------------
# Z = aX + bY + c 형태로 추정하거나, Ax + By + Cz + D = 0 추정
# 여기서는 단순화를 위해 Z 축을 종속 변수로 두고 평면 피팅 예시
X_floor = mvs_points[:, :2]  # X, Y
y_floor = mvs_points[:, 2]   # Z

ransac = RANSACRegressor(LinearRegression())
ransac.fit(X_floor, y_floor)

# 바닥면 인라이어 추출 (노이즈 제거)
inlier_mask = ransac.inlier_mask_
floor_points = mvs_points[inlier_mask]

# 바닥면의 평균 Z 값을 기준면 (Z=0 으로 재정의하기 위함) 으로 사용 가능
floor_z_mean = np.mean(floor_points[:, 2])
# 실제 파이프라인에서는 평면 법선을 구해 좌표계를 회전시키는 것이 더 정확합니다.
# (여기서는 설명의 편의를 위해 Z 기준 슬라이싱으로 가정)

# ---------------------------------------------------------
# 2. 단면별 원형 적합 (Circular Fitting per Section)
# ---------------------------------------------------------
section_heights = np.arange(floor_z_mean, floor_z_mean + 10, 0.5) # 0.5m 간격
circle_centers = []

for z in section_heights:
    # 해당 높이의 점들 추출 (반경 내 버퍼 허용, 예: ±0.1m)
    section_points = mvs_points[np.abs(mvs_points[:, 2] - z) < 0.1]
    
    if len(section_points) < 10: continue # 점이 너무 적으면 스킵
    
    xy_points = section_points[:, :2]
    
    # 원형 적합 (간단한 Least Squares Circle Fit 예시)
    # 실제 구현은 algebraic fit 이나 geometric fit 사용 권장
    # 여기서는 중심점 (mean) 과 평균 반경을 근사적으로 사용 (실제 논문은 더 정교한 알고리즘 사용)
    center = np.mean(xy_points, axis=0)
    radii = np.sqrt(np.sum((xy_points - center)**2, axis=1))
    mean_radius = np.mean(radii)
    
    # 단, 실제 원형 적합은 (a, b, r) 을 최적화해야 함
    # 여기서는 개념적으로 중심점만 저장
    circle_centers.append([center[0], center[1], z])

circle_centers = np.array(circle_centers)

# ---------------------------------------------------------
# 3. 중심축 추정 (Central Axis Estimation)
# ---------------------------------------------------------
if len(circle_centers) > 2:
    # PCA 를 사용하여 중심점들이 이루는 방향 (직선) 추정
    pca = PCA(n_components=3)
    pca.fit(circle_centers)
    
    # 제 1 주성분이 직선의 방향 벡터
    axis_direction = pca.components_[0]
    
    # 중심점은 중심점들의 평균 (무게중심)
    axis_point = np.mean(circle_centers, axis=0)
    
    print(f"Center Axis Point: {axis_point}")
    print(f"Center Axis Direction: {axis_direction}")
    
    # 수직도 분석 (방향 벡터와 Z 축 [0,0,1] 의 각도)
    z_axis = np.array([0, 0, 1])
    cos_angle = np.dot(axis_direction, z_axis) / (np.linalg.norm(axis_direction) * np.linalg.norm(z_axis))
    angle_deg = np.degrees(np.arccos(np.clip(cos_angle, -1.0, 1.0)))
    print(f"Deviation from Vertical (Degrees): {angle_deg}")

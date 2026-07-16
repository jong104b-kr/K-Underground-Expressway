[촬영] 
  ↓ (체커보드 보정 영상 포함 권장)
[카메라 보정 (Calibration)] 
  → 내부 파라미터 (K, D) 획득 (앞서 안내드린 단계)
  ↓
[특징점 매칭 (Feature Matching)] 
  → SuperPoint+LightGlue 등 사용 (앞서 안내드린 단계)
  ↓
[Structure from Motion (SfM)] 
  → 카메라 자세 (R, t), 희소 점군, 보정된 내부 파라미터 확정
  (도구: COLMAP, OpenMVG, Metashape 등)
  ↓ [SfM 결과: cameras.bin, points3D.bin, images.txt 등]
[Multi-View Stereo (MVS)] 
  1. 이미지 왜곡 제거 (Undistort)
  2. 깊이 맵 추정 (Depth Estimation)
  3. 점군 융합 (Fusion)
  4. 메쉬 생성 (Meshing)
  (도구: OpenMVS, COLMAP Dense, ODM 등)
  ↓
[후처리 (Post-processing)]
  → 메쉬 간소화 (Decimation)
  → 텍스처 매핑 (Texturing)
  → 구멍 메우기 (Hole Filling)
  → 3D 포맷 변환 (OBJ, PLY, GLTF 등)

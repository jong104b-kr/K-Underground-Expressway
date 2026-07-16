import cv2
import numpy as np
import glob

# 1. 체커보드 설정 (행, 열 수)
ROWS = 9
COLS = 6

# 3D 객체 점 준비 (Z=0 평면)
objp = np.zeros((ROWS * COLS, 3), np.float32)
objp[:, :2] = np.mgrid[0:COLS, 0:ROWS].T.reshape(-1, 2)

objpoints = []  # 3D 점 저장
imgpoints = []  # 2D 점 저장

# 2. 이미지 로드 및 코너 탐지
images = glob.glob('calibration_images/*.jpg') # 보정 이미지 폴더

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 체커보드 코너 찾기
    ret, corners = cv2.findChessboardCorners(gray, (COLS, ROWS), None)

    if ret:
        objpoints.append(objp)
        
        # 서브픽셀 정확도를 위해 코너 위치 정밀화
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)

        # 시각화 (선택 사항)
        cv2.drawChessboardCorners(img, (COLS, ROWS), corners2, ret)
        cv2.imshow('img', img)
        cv2.waitKey(500)

cv2.destroyAllWindows()

# 3. 보정 수행
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# 4. 결과 출력
print("Camera Matrix (K):\n", mtx)
print("Distortion Coefficients (D):\n", dist)

# 5. 왜곡 보정 적용 예시
img = cv2.imread('test_image.jpg')
h, w = img.shape[:2]
# 새로운 카메라 행렬 생성 (최적화된 시야각)
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

# undistort 적용
dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
# 불필요한 ROI 잘라내기
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv2.imwrite('calibratesan.jpg', dst)

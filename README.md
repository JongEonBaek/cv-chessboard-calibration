# 🎯 Camera Calibration & Real-time Distortion Correction

이 프로젝트는 체스보드(Checkerboard) 패턴을 이용해 카메라의 내부 파라미터(Camera Intrinsic Matrix, K) 및 왜곡 계수(Distortion Coefficients)를 계산하고, 이를 이용하여 비디오의 렌즈 왜곡을 실시간으로 보정하여 시각적으로 비교할 수 있도록 만든 OpenCV 기반의 도구입니다.

---

## 🧭 기능 개요

### 📌 **체스보드 이미지 추출 및 카메라 보정**
- 비디오 영상에서 체스보드 패턴이 포함된 프레임을 수동으로 선택하여 저장
- 선택된 이미지를 이용해 OpenCV의 `calibrateCamera()` 함수로 카메라 보정 수행
- 계산된 결과(K, 왜곡 계수)를 출력

### 📌 **실시간 렌즈 왜곡 보정 시각화**
- 비디오에서 실시간으로 원본 영상과 왜곡 보정된 영상을 토글하며 비교 가능
- 일시정지 상태에서도 원본과 보정 영상을 전환하며 자세히 확인 가능

---

## 📂 파일 구성

```
.
├── data
│   └── recorded_video.avi (체스보드 영상 파일)
├── camera_calibration.py (체스보드 이미지 추출 및 카메라 보정 수행)
└── distortion_correction.py (실시간 왜곡 보정 시각화)
```

---

## 🛠️ 사용 방법

### 📌 **카메라 보정 실행**

```bash
python camera_calibration.py
```

- `Space`: 체스보드 코너 감지
- `Enter`: 현재 프레임 이미지 선택
- `ESC`: 이미지 선택 종료 후 보정 결과 출력

### 📌 **왜곡 보정 시각화 실행**

```bash
python distortion_correction.py
```

- `Space`: 일시정지 / 재생
- `Tab`: 원본 영상 ↔ 보정 영상 전환
- `ESC`: 프로그램 종료

---

## 📌 **카메라 보정 결과 예시**

```
Camera Calibration Results:
- Number of selected images: 12
- RMS error: 0.2145
- Camera Matrix (K):
  [[603.51030778   0.         674.89585317]
   [  0.         603.45260428 381.01122663]
   [  0.           0.           1.        ]]

- Distortion coefficients:
  [0.03412314, -0.16458017, 0.0032529, 0.00097189, 0.17881176]
```

---

## 🔍 기술적 특징
- OpenCV의 `findChessboardCorners()`로 체스보드 패턴 자동 검출
- `calibrateCamera()`로 카메라 행렬 및 왜곡 계수 계산
- `initUndistortRectifyMap()` 및 `remap()`을 이용한 효율적인 픽셀 재매핑
- 비디오 처리 시 회전 및 리사이징 기능 제공

---

## ⌨️ 단축키 안내

| 키       | 기능                  |
|----------|-----------------------|
| `Space`  | 재생 / 일시정지       |
| `Tab`    | 원본 ↔ 보정 영상 토글 |
| `ESC`    | 프로그램 종료         |

---

## ⚙️ 개발 환경
- Python 3.x
- OpenCV (cv2)
- NumPy

---

## ✨ 응용 분야
- 카메라 기반 로봇 비전 시스템
- 컴퓨터 비전 및 영상 분석 연구
- 실시간 영상 처리가 필요한 증강현실(AR) 애플리케이션

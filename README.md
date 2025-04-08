## Camera Calibration Results ( K 값 )
* Number of images: 7
* RMS error: 0.6548729256645048

* Camera matrix (K):
[[375.80862274   0.         189.74191902]
 [  0.         373.46722139 216.74330588]
 [  0.           0.           1.        ]]

* Distortion coefficients(왜곡 계수):
[-0.35423594  0.14330272  0.01454548 -0.00846743 -0.04192887]

## 왜곡 보정 결과
![image](https://github.com/user-attachments/assets/d67a1368-e796-4745-aeb1-921e4e06c235)
![image](https://github.com/user-attachments/assets/d26147fc-dfa1-4480-ba90-32fd219a15b4)


## 🧭 기능 개요

### 📌calibration.py : **체스보드 이미지 추출 및 카메라 보정**
- 비디오 영상에서 체스보드 패턴이 포함된 프레임을 수동으로 선택하여 저장
- 선택된 이미지를 이용해 OpenCV의 `calibrateCamera()` 함수로 카메라 보정 수행
- 계산된 결과(K, 왜곡 계수)를 출력

- `Space`: 체스보드 코너 감지
- `Enter`: 현재 프레임 이미지 선택
- `ESC`: 이미지 선택 종료 후 보정 결과 출력

### 📌 distortion.py : **실시간 렌즈 왜곡 보정 시각화**
- 비디오에서 실시간으로 원본 영상과 왜곡 보정된 영상을 토글하며 비교 가능
- 일시정지 상태에서도 원본과 보정 영상을 전환하며 자세히 확인 가능

- `Space`: 일시정지 / 재생
- `Tab`: 원본 영상 ↔ 보정 영상 전환
- `ESC`: 프로그램 종료

---


# 카메라 캘리브레이션 및 렌즈 왜곡 보정 프로그램입니다
# camera_calibration_with_distortion_correction

## 원본영상:
[[![chessboard.mp4](https://img.youtube.com/vi/VIDEO_ID/0.jpg)]](https://github.com/yunee19/camera_calibration_with_distortion_correction/assets/133479803/8f58ea9a-8ec2-47c9-a7e8-362fbc3eec37)

## 실행 결과 demo 이미지:
![camera_calibration_with_distortion_correction_result_demo01](https://github.com/yunee19/camera_calibration_with_distortion_correction/assets/133479803/a377ccbe-f919-446e-8f8a-724f8f89d0a3)
![camera_calibration_with_distortion_correction_result_demo02](https://github.com/yunee19/camera_calibration_with_distortion_correction/assets/133479803/3782055d-181b-469c-ac19-5eab12f0e818)
![camera_calibration_with_distortion_correction_result_demo04](https://github.com/yunee19/camera_calibration_with_distortion_correction/assets/133479803/e5a317df-7e32-452d-8e09-aef0d606a12f)
![camera_calibration_with_distortion_correction_result_demo03](https://github.com/yunee19/camera_calibration_with_distortion_correction/assets/133479803/5749d0af-72f5-4d5f-bef0-1e43ed16d4d3)

이 프로그램은 OpenCV를 사용하여 체스보드 패턴을 활용한 카메라 캘리브레이션과 함께 렌즈 왜곡 보정을 수행합니다.

### 카메라 캘리브레이션 기능 :

- 비디오 파일에서 각 프레임을 읽습니다.
- 회색조 이미지로 변환한 후, 체스보드 코너를 찾습니다.
- 코너를 찾으면 객체 지점과 이미지 지점을 저장하고, 카메라 캘리브레이션을 수행합니다.
- 카메라 캘리브레이션 결과를 사용하여 프레임의 렌즈 왜곡을 보정합니다.

### 렌즈 왜곡 보정 기능 :

- 캘리브레이션 결과를 이용하여 프레임의 렌즈 왜곡을 보정합니다.
- `cv.undistort()` 함수를 사용하여 렌즈 왜곡을 보정하고, 보정된 프레임을 생성합니다.
- 보정된 프레임을 새로운 비디오 파일에 저장하고, 화면에 표시합니다.

**간단한 흐름:**

1. 비디오 파일 열기
2. 각 프레임에서 코너 찾기
3. 코너가 발견되면 객체 및 이미지 지점 저장 및 카메라 캘리브레이션 수행
4. 렌즈 왜곡 보정하여 보정된 프레임 생성
5. 보정된 프레임 저장 및 표시
6. 작업이 완료되면 비디오 파일과 창 닫기

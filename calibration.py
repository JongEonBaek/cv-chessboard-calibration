import numpy as np
import cv2 as cv

def extract_chessboard_images(video_path, pattern_size, auto_select=False, wait=10, window_name='Camera Calibration', scale=0.7):
    video = cv.VideoCapture(video_path)
    selected_images = []

    while True:
        ret, frame = video.read()
        if not ret:
            break

        frame = cv.rotate(frame, cv.ROTATE_90_COUNTERCLOCKWISE)
        frame = cv.resize(frame, None, fx=scale, fy=scale)

        if auto_select:
            selected_images.append(frame)
            continue

        display = frame.copy()
        msg = f'Selected: {len(selected_images)}  [Space: detect] [Enter: save] [ESC: exit]'
        cv.putText(display, msg, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))
        cv.imshow(window_name, display)

        key = cv.waitKey(wait)
        if key == ord(' '):
            found, corners = cv.findChessboardCorners(frame, pattern_size)
            cv.drawChessboardCorners(display, pattern_size, corners, found)
            cv.imshow(window_name, display)
            if cv.waitKey() in [13, ord('\n'), ord('\r')]:  # Enter
                selected_images.append(frame)
        elif key == 27:  # ESC
            break

    cv.destroyAllWindows()
    return selected_images

def run_camera_calibration(images, pattern_size, cell_size, K=None, dist_coeff=None, flags=None):
    img_points = []
    for img in images:
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        found, corners = cv.findChessboardCorners(gray, pattern_size)
        if found:
            img_points.append(corners)

    obj_template = np.array([[c, r, 0] for r in range(pattern_size[1]) for c in range(pattern_size[0])], dtype=np.float32) * cell_size
    obj_points = [obj_template] * len(img_points)

    return cv.calibrateCamera(obj_points, img_points, gray.shape[::-1], K, dist_coeff, flags=flags)

if __name__ == '__main__':
    video_path = 'data/recorded_video.avi'
    pattern_size = (8, 6)
    cell_size = 0.022

    selected_images = extract_chessboard_images(video_path, pattern_size)
    if len(selected_images) == 0:
        print('선택된 이미지가 없습니다.')
        exit()

    rms, K, dist_coeff, rvecs, tvecs = run_camera_calibration(selected_images, pattern_size, cell_size)

    print('## Camera Calibration Results')
    print(f'* Number of images: {len(selected_images)}')
    print(f'* RMS error = {rms}')
    print(f'* Camera matrix (K):\n{K}')
    print(f'* Distortion coefficients: {dist_coeff.flatten()}')

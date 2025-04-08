import numpy as np
import cv2 as cv

def load_video(video_path):
    cap = cv.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError(f"Cannot open video file: {video_path}")
    return cap

def preprocess_frame(frame, scale=0.7):
    frame = cv.rotate(frame, cv.ROTATE_90_COUNTERCLOCKWISE)
    return cv.resize(frame, None, fx=scale, fy=scale)

def generate_undistort_maps(K, dist_coeffs, image_size):
    return cv.initUndistortRectifyMap(
        K, dist_coeffs, None, None, image_size, cv.CV_32FC1
    )

def undistort_image(image, map1, map2):
    return cv.remap(image, map1, map2, interpolation=cv.INTER_LINEAR)

def display_frame_with_text(window_name, image, text):
    output = image.copy()
    cv.putText(output, text, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))
    cv.imshow(window_name, output)

def interactive_pause(window_name, original_img, rectified_img, map1, map2):
    show_rectified = True
    current_img = rectified_img

    while True:
        display_frame_with_text(window_name, current_img,
                                "Rectified" if show_rectified else "Original")
        key = cv.waitKey(0)

        if key == ord(' '):  # Resume
            return show_rectified
        elif key == 27:  # ESC
            cv.destroyAllWindows()
            exit()
        elif key == ord('\t'):  # Toggle
            show_rectified = not show_rectified
            current_img = rectified_img if show_rectified else original_img

def main():
    video_path = 'data/recorded_video.avi'
    window_name = 'Geometric Distortion Correction'

    # Camera calibration parameters
    K = np.array([[375.80862274, 0, 189.74191902],
                  [0, 373.46722139, 216.74330588],
                  [0, 0, 1]])

    dist_coeffs = np.array([-0.35423594, 0.14330272,
                             0.01454548, -0.00846743,
                             -0.04192887])

    resize_scale = 0.7
    show_rectified = True
    map1, map2 = None, None

    video = load_video(video_path)

    while True:
        ret, frame = video.read()
        if not ret:
            video.set(cv.CAP_PROP_POS_FRAMES, 0)
            continue

        processed = preprocess_frame(frame, scale=resize_scale)
        original_img = processed.copy()

        if show_rectified:
            if map1 is None or map2 is None:
                map1, map2 = generate_undistort_maps(
                    K, dist_coeffs, (original_img.shape[1], original_img.shape[0]))
            display_img = undistort_image(original_img, map1, map2)
            info = "Rectified"
        else:   
            display_img = original_img
            info = "Original"

        display_frame_with_text(window_name, display_img,
                                f"{info} | Space: pause | Tab: toggle | ESC: exit")

        key = cv.waitKey(10)
        if key == ord(' '):
            rectified_img = display_img.copy()
            show_rectified = interactive_pause(
                window_name, original_img, rectified_img, map1, map2)
        elif key == 27:  # ESC
            break
        elif key == ord('\t'):  # Tab
            show_rectified = not show_rectified

    video.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()

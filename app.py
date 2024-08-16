import cv2
import os

def extract_frames(video_path, output_dir='./img/'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    video_capture = cv2.VideoCapture(video_path)

    if not video_capture.isOpened():
        print("Не удалось открыть видеофайл.")
        return

    frame_count = 0
    while True:
        success, frame = video_capture.read()

        if not success:
            break

        frame_filename = os.path.join(output_dir, f'{frame_count}.png')
        cv2.imwrite(frame_filename, frame)

        frame_count += 1

    video_capture.release()
    print(f"Разделение завершено. Всего извлечено {frame_count} кадров.")

video_path = '.video/video.mp4' 
extract_frames(video_path)

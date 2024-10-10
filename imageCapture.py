import cv2

def detect_bounding_box(vid):
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

def video_capture_script(log_file_name):
    import logFile
    x = int(input("Select a device: \n"+"1. PC webcam\n"+"2. Mobile as webcam\n"))
    if x==1:
        logFile.write_to_log("Using PC Webcam.",log_file_name)
        video_capture = cv2.VideoCapture(0)
    elif x==2:
        logFile.write_to_log("Using smartphone as Webcam.",log_file_name)
        video_capture = cv2.VideoCapture(1)
    else:
        logFile.write_to_log("Invalid Input",log_file_name)
        import sys,os
        os.remove(log_file_name)
        sys.exit()

    frame_counter = 0
    frame_skip_interval = 3  # Adjust this value based on your requirements
    while True:
        result, video_frame = video_capture.read()
        if result is False:
            break

        frame_counter += 1
        if frame_counter % frame_skip_interval != 0:
            continue  # Skip processing this frame

        faces = detect_bounding_box(video_frame)
        cv2.imshow("Image_capture", video_frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        elif key == 32:  # 32 corresponds to the spacebar key
            cv2.imwrite("captured_image.jpg", video_frame)
            print("Image captured!")
            logFile.write_to_log("Image captured",log_file_name)
            break

    video_capture.release()
    cv2.destroyAllWindows()

    return 'captured_image.jpg'
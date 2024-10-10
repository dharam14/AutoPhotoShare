def image_resizer(image):
    import cv2
    height, width = image.shape[:2]
    new_width = 360  # Lower value gives speed
    new_height = int((new_width / width) * height)
    resized_image = cv2.resize(image, (new_width, new_height))

    return resized_image

def similar_images(captured_image_path, directory_path, log_file_name):
    import logFile
    matched_images_path = []

    from faceDetection import find_face_encodings
    captured_image_encodings = find_face_encodings(captured_image_path)
    if captured_image_encodings is None:
        import sys, os
        logFile.write_to_log("Face not detected in captured image", log_file_name)
        os.remove(log_file_name)
        sys.exit()

    from loadImg import image_loader
    import cv2
    import face_recognition
    images = image_loader(directory_path)
    for image_path, image in images:
        resized_image = image_resizer(image)  # Resizing image

        cv2.imshow("Image", resized_image)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break
        directory_image_encodings = find_face_encodings(image_path)  # image loaded from directory

        if directory_image_encodings is None:
            logFile.write_to_log(f"Face not detected on image: {image_path}", log_file_name)
            continue

        is_same = face_recognition.compare_faces([captured_image_encodings], directory_image_encodings)[0]  # checking both images are same
        print(f"Is Same: {is_same}")
        logFile.write_to_log(f"Is same: {is_same} -> {image_path}", log_file_name)
        if is_same:
            matched_images_path.append(image_path)
            # Calculating accuracy level between images
            distance = face_recognition.face_distance([captured_image_encodings], directory_image_encodings)
            distance_value = round(distance[0] * 100)
            accuracy = 100 - distance_value
            print(f"Accuracy Level: {accuracy}%")
            logFile.write_to_log(f"Distance: {distance_value}, Accuracy: {accuracy}", log_file_name)
        continue
    cv2.destroyAllWindows()

    matched_images_path.append(captured_image_path)
    if matched_images_path:
        return matched_images_path
    else:
        return None

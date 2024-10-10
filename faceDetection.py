def find_face_encodings(image_path):
    import cv2
    import face_recognition

    image = cv2.imread(image_path) # reading image
    face_enc = face_recognition.face_encodings(image) # get face encodings from the image
    if face_enc:
        return face_enc[0] # return face encodings
    else:
        return None
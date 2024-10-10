def image_loader(directory_path):
    import os
    import cv2

    image_files = [f for f in os.listdir(directory_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    images = []
    for image_file in image_files:
        image_path = os.path.join(directory_path, image_file)
        img = cv2.imread(image_path)
        if img is not None:
            images.append((image_path, img))

    return images
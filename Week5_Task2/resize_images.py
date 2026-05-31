import cv2
import os

folders = [
    ("dataset/images/train", "dataset/images/train_resized"),
    ("dataset/images/val", "dataset/images/val_resized")
]

for src, dst in folders:
    os.makedirs(dst, exist_ok=True)

    for file in os.listdir(src):
        img = cv2.imread(os.path.join(src, file))

        h, w = img.shape[:2]
        new_w = 384
        new_h = int(h * (384 / w))

        resized = cv2.resize(img, (new_w, new_h))

        cv2.imwrite(os.path.join(dst, file), resized)

print("Resizing completed!")
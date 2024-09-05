import os
import shutil


def get_images(root, cam1, cam2):
    imgs = {cam1: [], cam2: []}
    for img in os.listdir(root):
        imgs[img.split('_')[0]].append(os.path.join(root, img))
    imgs[cam1].sort(key=lambda x: int(os.path.basename(x).split('_')[1].split('.')[0]))
    imgs[cam2].sort(key=lambda x: int(os.path.basename(x).split('_')[1].split('.')[0]))

    return imgs


def remove_frame_offset(root, offset):
    for k, v in offset.items():
        for i in range(v):
            img_name = os.path.join(root, f"{k}_{i}.png")
            if os.path.exists(img_name):
                os.remove(img_name)

    images = get_images(root, *offset.keys())

    for k in offset.keys():
        for img in images[k]:
            cam = os.path.basename(img).split('_')[0]
            num = int(os.path.basename(img).split('_')[1].split('.')[0])
            shutil.copy(os.path.join(root, img), os.path.join(root, f"{cam}_{num - offset[cam]}.png"))
            os.remove(os.path.join(root, img))


if __name__ == "__main__":
    root = r'/home/alex/Projects/Mobil-Group/military-obj-cv-detection/src/find_ccordinates_by_cameras/calib_recordings/frames_1_3'
    offset = {
        '1': 3,
        '3': 1,
    }

    remove_frame_offset(root, offset)

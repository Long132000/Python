import os

import cv2
import numpy as np

from src.find_ccordinates_by_cameras.image_transformation_utils.delete_unpair import delete_unpair


def get_images(root, cam1, cam2):
    imgs = {cam1: [], cam2: []}
    for img in os.listdir(root):
        imgs[img.split('_')[0]].append(os.path.join(root, img))
    imgs[cam1].sort(key=lambda x: int(os.path.basename(x).split('_')[1].split('.')[0]))
    imgs[cam2].sort(key=lambda x: int(os.path.basename(x).split('_')[1].split('.')[0]))

    return imgs


# CONFIG

root = r'/home/alex/Projects/Mobil-Group/military-obj-cv-detection/src/find_ccordinates_by_cameras/calib_recordings/frames_1_3'
cam1, cam2 = '1', '3'

n, m = 10, 10  # где n и m - размерность шахматной доски
num_frames = 10
# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# MAIN SCRIPT

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
# Здесь 9 и 9 - размеры искомой в кадре шахматной доски, которые определяются в зависимости от используемого изображения
# Необходимо брать значения типа (n-1)*(m-1),
n, m = n - 1, m - 1
objp = np.zeros((n * m, 3), np.float32)
objp[:, :2] = np.mgrid[0:n, 0:m].T.reshape(-1, 2)

# MAIN SCRIPT
delete_unpair(root, cam1, cam2)

images = get_images(root, cam1, cam2)
cam1_imgs, cam2_imgs = images[cam1], images[cam2]

for cam1_img, cam2_img in zip(cam1_imgs, cam2_imgs):
    while True:
        # Read and transform the image
        img1 = cv2.imread(cam1_img)
        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        width = img1.shape[1]
        height = img1.shape[0]

        img2 = cv2.imread(cam2_img)
        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        # Find the chess board corners
        ret_chess1, corners1 = cv2.findChessboardCorners(gray1, (n, m),
                                                         flags=cv2.CALIB_CB_EXHAUSTIVE + cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_NORMALIZE_IMAGE)

        ret_chess2, corners2 = cv2.findChessboardCorners(gray2, (n, m),
                                                         flags=cv2.CALIB_CB_EXHAUSTIVE + cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_NORMALIZE_IMAGE)

        if ret_chess1 and ret_chess2:
            corners1_2 = cv2.cornerSubPix(gray1, corners1, (11, 11), (-1, -1), criteria)
            corners2_2 = cv2.cornerSubPix(gray2, corners2, (11, 11), (-1, -1), criteria)

            cv2.drawChessboardCorners(img1, (n, m), corners1_2, ret_chess1)
            cv2.drawChessboardCorners(img2, (n, m), corners2_2, ret_chess2)
        else:
            print('Delete pair, because one of the chess board is not recognized!')
            os.remove(cam1_img)
            os.remove(cam2_img)
            break

        cv2.imshow(f'Camera {cam1} Calibration', img1)
        cv2.imshow(f'Camera {cam2} Calibration', img2)

        k = cv2.waitKey(0)

        if k == ord('s'):
            print('Next pair ...')
            break

        if k == ord('r'):
            print('Choose which one rotate: ')
            k2 = cv2.waitKey(0)
            if k2 == ord(','):
                image = cv2.rotate(img1, cv2.ROTATE_180)
                cv2.imwrite(cam1_img, image)
            else:
                image = cv2.rotate(img2, cv2.ROTATE_180)
                cv2.imwrite(cam2_img, image)

        if k == ord('d'):
            print('Delete pair...')
            os.remove(cam1_img)
            os.remove(cam2_img)
            break

import os


def delete_unpair(root, cam1, cam2):
    files = os.listdir(root)
    for file in files:
        cam = file.split("_")[0]
        num = file.split("_")[1].split('.')[0]
    
        if f"{cam1 if cam == cam2 else cam2}_{num}.png" not in files:
            os.remove(os.path.join(root, file))
            print(f'Delete {os.path.join(root, file)}')


if __name__ == "__main__":
    cam1, cam2 = '3', '4'
    root = 'calib_recordings/frames_3_4'
    delete_unpair(root, cam1, cam2)
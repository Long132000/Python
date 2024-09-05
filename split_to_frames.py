import cv2
import os


def split_to_folder(video_path, output_folder, cam):
    print(f'Splitting video: {video_path} into {output_folder} for cam: {cam}')
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video file was opened successfully
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        exit()

    frame_count = 0
    n = 5
    c = 0
    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        c += 1

        if c % n != 0:
            continue

        # If the frame was not read successfully, break the loop
        if not ret:
            break

        # Construct the filename for the current frame
        frame_filename = os.path.join(output_folder, f'{cam}_{frame_count}.png')

        # Save the current frame as an image file
        cv2.imwrite(frame_filename, frame)

        # Increment the frame count
        frame_count += 1

    # Release the video capture object
    cap.release()

    print(f'Total frames saved: {frame_count}')


if __name__ == "__main__":
    # Path to the video file
    cam1 = 1
    cam2 = 3

    # Path to the folder where frames will be saved
    output_folder = f'calib_recordings/frames_{cam1}_{cam2}'

    split_to_folder(f'calib_recordings/camera_num_{cam1}.mp4', output_folder, str(cam1))
    split_to_folder(f'calib_recordings/camera_num_{cam2}.mp4', output_folder, str(cam2))

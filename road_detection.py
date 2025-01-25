from ultralytics import YOLO
import cv2
import os


model_path = "C:/D MOVED FILE/prototype/Yolo-Weights/runs/segment/train4/weights/last.pt"


def getFrame(video_path):
    # Folder to save the extracted frames
    output_folder = 'mask'

    # Create the folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video file.")
        exit()

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Select 4 evenly spaced frames
    frames_to_extract = [int(total_frames * i / 5) for i in range(1, 5)]

    # Loop through the video and save the selected frames
    frame_count = 0
    extracted_frames = 0

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        if frame_count in frames_to_extract:
            # Save the frame as an image file in the 'mask' folder
            frame_filename = os.path.join(output_folder, f'car_{extracted_frames + 1}.jpg')
            cv2.imwrite(frame_filename, frame)
            print(f"Saved {frame_filename}")
            extracted_frames += 1

        frame_count += 1

        if extracted_frames == 2:
            break

    # Release the video capture object
    cap.release()
    cv2.destroyAllWindows()


def trainMask(image1,image2,image3,image4):

    # image_path = 'frame_0.jpg'

    img1 = cv2.imread("frame_1.jpg")
    H, W, _ = img1.shape

    model = YOLO(model_path)

    results = model(img1)

    for result in results:
        for j, mask in enumerate(result.masks.data):
            mask = mask.numpy() * 255

            mask = cv2.resize(mask, (W, H))

            cv2.imwrite('.output/output1.png', mask)

    img2 = cv2.imread(image2)
    H, W, _ = img2.shape

    model = YOLO(model_path)

    results = model(img2)

    for result in results:
        for j, mask in enumerate(result.masks.data):
            mask = mask.numpy() * 255

            mask = cv2.resize(mask, (W, H))

            cv2.imwrite('.output/output2.png', mask)

    img3 = cv2.imread(image3)
    H, W, _ = img3.shape

    model = YOLO(model_path)

    results = model(img3)

    for result in results:
        for j, mask in enumerate(result.masks.data):
            mask = mask.numpy() * 255

            mask = cv2.resize(mask, (W, H))

            cv2.imwrite('.output/output3.png', mask)

    img4 = cv2.imread(image4)
    H, W, _ = img4.shape

    model = YOLO(model_path)

    results = model(img4)

    for result in results:
        for j, mask in enumerate(result.masks.data):
            mask = mask.numpy() * 255

            mask = cv2.resize(mask, (W, H))

            cv2.imwrite('.output/output4.png', mask)

getFrame("videos/c5.mp4")

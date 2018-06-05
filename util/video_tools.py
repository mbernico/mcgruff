import cv2
import os


def video_to_images(video_file, output_dir, frame_count=10):
    vidcap = cv2.VideoCapture(video_file)
    success, image = vidcap.read()
    count = 0

    if frame_count < 1:
        raise ValueError("frame_count must be > 0 ")

    while success:
        if count % frame_count == 0:
            out_name = os.path.join(output_dir, "frame%d.jpg" % count)
            cv2.imwrite(out_name, image)
        count += 1
        success, image = vidcap.read()


def images_to_video(img_list, video_filename, frame_rate=10):
    first_image = cv2.imread(img_list[0])
    height, width, layers = first_image.shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(video_filename, fourcc, frame_rate, (width, height))

    for image in img_list:
        video.write(cv2.imread(image))
    cv2.destroyAllWindows()
    video.release()







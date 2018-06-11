from util.video_tools import images_to_video
from pathlib import Path


def sort_images(images):
    return sorted(images, key=lambda x: int("".join([str(s) for s in x if s.isdigit()])))


def glob_yolo_predictions():
    predictions_glob = Path.cwd().joinpath("annotated_predictions").glob("*.jpg")
    return [str(x) for x in predictions_glob]


def main():  # pragma: no cover
    predictions = glob_yolo_predictions()
    predictions = sort_images(predictions)
    images_to_video(predictions, "video.mp4", frame_rate=30)


if __name__ == "__main__":
    main()

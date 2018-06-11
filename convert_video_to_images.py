from util.video_tools import video_to_images
from pathlib import Path


def main():  # pragma: no cover
    outpath = str(Path.cwd().joinpath("Images").joinpath("002"))
    video = str(Path.cwd().joinpath("video").joinpath("20180603_195607.mp4"))
    video_to_images(video, outpath, frame_count=1)


if __name__ == "__main__":
    main()

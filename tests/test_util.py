import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from util.video_tools import *


def test_video_to_images(tmpdir):
    p = tmpdir.mkdir("outdir")
    video_to_images("./Wildlife.mp4", p, frame_count=10)
    assert len(p.listdir()) == 91


def test_images_to_video(tmpdir):
    p = tmpdir.mkdir("outdir")
    video_to_images("./Wildlife.mp4", p, frame_count=10)
    images = [str(x) for x in p.listdir()]
    images.sort()
    images_to_video(images, str(p.join("test_video.mp4")))
    assert "test_video.mp4" in str(p.listdir())

## Taking a bite out of crime


## Workflow

1.  slice video into frames using convert_video_to_images.py whenever Jeff writes it.  Store images in Image/002
2.  Run BBox, input 002 and press load, label images...
3.  Move all images from Images/002 and labels from Labels/002 into ./data
4.  Run tk2yolo.py
5.  run copy_labeled_data.sh to copy only the labeled images and data into ./labeled_data


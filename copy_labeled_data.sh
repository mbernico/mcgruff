#!/bin/bash

SOURCE_DIR="./data"
DEST_DIR="./labeled_data"

for file in $SOURCE_DIR/*_yolo.txt; do
  cp ${file/_yolo.txt/.jpg} $DEST_DIR/;
  cp $file $DEST_DIR;
done

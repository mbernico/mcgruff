#!/bin/bash

for file in /data/users/qepz/mcgruff/labeled_data/*.jpg;
  do
  ./darknet detector test /data/users/qepz/mcgruff/mcgruff.data /data/users/qepz/mcgruff/mcgruff.cfg /data/users/qepz/mcgruff/backup/mcgruff.backup ${file};
  mv predictions.jpg ${file/.jpg/_prediction.jpg};
done

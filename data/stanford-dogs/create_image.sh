#!/usr/bin/env sh
# Create the imagenet lmdb inputs
# N.B. set the path to the imagenet train + val data dirs
DATASET_NAME=stanford-dogs
DATASET_ROOT=.
IMAGE_ROOT=$DATASET_ROOT/dog_detected/

# Set RESIZE=true to resize the images to 256x256. Leave as false if images have
# already been resized using another tool.
RESIZE=true
if $RESIZE; then
  RESIZE_HEIGHT=256
  RESIZE_WIDTH=256
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi

echo "Creating train lmdb..."

GLOG_logtostderr=1 convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $IMAGE_ROOT \
    $DATASET_ROOT/train.txt \
    $DATASET_ROOT/${DATASET_NAME}_train_lmdb

echo "Creating val lmdb..."

GLOG_logtostderr=1 convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $IMAGE_ROOT \
    $DATASET_ROOT/val.txt \
    $DATASET_ROOT/${DATASET_NAME}_val_lmdb

echo "Done."

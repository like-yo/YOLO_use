#!/bin/bash
# rm -rf runs/*

python train.py  --cfg models/yolov5n.yaml --data data/yolo_locount.yaml --epoch 50 --batch-size 16 --imgsz 640
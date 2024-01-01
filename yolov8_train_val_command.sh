#!/bin/bash
# rm -rf runs/*
# 官网说明：https://docs.ultralytics.com/zh/modes/train/#_2

# train:

# 从YAML构建新模型，从头开始训练
yolo detect train data=coco128.yaml model=yolov8n.yaml epochs=100 imgsz=640

# 从预训练*.pt模型开始训练
yolo detect train data=coco128.yaml model=yolov8n.pt epochs=100 imgsz=640

# 从YAML构建一个新模型，转移预训练权重，然后开始训练
yolo detect train data=coco128.yaml model=yolov8n.yaml pretrained=yolov8n.pt epochs=100 imgsz=640



# val: 

yolo detect val model=yolov8n.pt  # 验证官方模型
yolo detect val model=path/to/best.pt  # 验证自定义模型



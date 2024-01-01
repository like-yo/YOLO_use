from ultralytics import YOLO
# model=YOLO(r'runs\detect\train4\weights\best.pt')
# 加载一个模型
model = YOLO('yolov8.yaml')  # 从YAML建立一个新模型
model = YOLO('yolov8n.pt')  # 加载预训练模型（推荐用于训练）
model = YOLO('yolov8n.yaml').load('yolov8n.pt')  # 从YAML建立并转移权重

# # 训练模型
results = model.train(data='dataset.yaml', epochs=100)
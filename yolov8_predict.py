from ultralytics import YOLO
import cv2
# 加载模型
# model = YOLO(r'runs\detect\train4\weights\best.pt')  # 预训练的 YOLOv8n 模型
model = YOLO(r'yolov8n.pt')
# 在图片列表上运行批量推理
results = model.predict('/root/autodl-tmp/pch/yolov8/1/images/test/bird_431.jpg',save=True)#, r'D:\pitcture_of_text\bird_test2.jpeg'])  # 返回 Results 对象列表
# k=model('/root/autodl-tmp/pch/yolov8/1/images/test/bird_431.jpg',  imgsz=320, conf=0.5)[0].plot()#返回一个带有绘制结果的三维BGR数组
# print(k,type(k))
# cv2.imshow('bb',k)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 处理结果列表
# for result in results:
#     boxes = result.boxes  # 边界框输出的 Boxes 对象
#     masks = result.masks  # 分割掩码输出的 Masks 对象
#     keypoints = result.keypoints  # 姿态输出的 Keypoints 对象
#     probs = result.probs  # 分类输出的 Probs 对象

cp runs/train/exp/weights/best.pt .
python train.py  --cfg models/yolov5n.yaml --data data/yolo_locount.yaml --epoch 50 --batch-size 16 --imgsz 640
python val.py --weights best.pt --data data/NEU-DET.yaml --task val

python val.py --weights best.pt --data data/NEU-DET.yaml --task test

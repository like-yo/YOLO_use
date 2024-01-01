
cp runs/train/exp/weights/best.pt .

python val.py --weights best.pt --data data/NEU-DET.yaml --task val

python val.py --weights best.pt --data data/NEU-DET.yaml --task test
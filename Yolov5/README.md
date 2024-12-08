

yolov5: https://github.com/ultralytics/yolov5.git

``` python train.py --data data.yaml --epochs 10 --weights '' --cfg yolov5l.yaml --batch-size -1 --name ```

### dataset
- Pattern
-   mask -> 白色地放的位置 pattern -> 白色方塊
一開始有設定img_shape 但是data 每一張都不一樣
 -> 依照每一張讀進來的圖片去更改mask的大小
 -> 配合每個圖片的label位置 去將mask=1標出來 (原本badnet統一在整張圖片右下角)
``` python detect.py --weights --source --classes= --save-csv ```


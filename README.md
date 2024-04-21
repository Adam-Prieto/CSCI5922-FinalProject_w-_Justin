# CSCI 5922 - Final Project (Adam & Justin)

## Updates (As they occur)

### April 12 - Adam
Fully trained YoloV8 model on African Animal dataset after much headache. My next step is to get this model working with others from the google doc page. Also, training
the model on 100 epoch took a lot longer than I would've guessed. Would not recommend.

### April 14 - Adam 
* More models are located [here](https://github.com/open-mmlab/mmdetection?tab=readme-ov-file#overview-of-benchmark-and-model-zoo).
* Loading models with mmdet runs into an installation error: NotImplementedError: A UTF-8 locale is required. Got ANSI_X3.4-1968. This error severly impacts loading pretrained models into google colab.
* [Link](https://github.com/open-mmlab/mmdetection/tree/main/configs/rtmdet) tries to work through installation, looking into now. 

---

## Metrics for Object Detection Models
This section contains the mAP, inference times, and memory usage during inference for each model. Fill in the blanks under each model name the output of running the inference command and provided configuration files located in the `mmdetection/configs/african-wildlife` directory. To obtain these metrics, follow these steps:

1. Download the [weights of the models](https://o365coloradoedu-my.sharepoint.com/:f:/g/personal/jung5864_colorado_edu/EuUUd68bKmVIjZiH52WXiRIBtcMcpPFJhK_UaK0vUjXAGQ?e=EeW5mr) trained by Justin.
2. Download the configuration files in the `mmdetection/configs/african-wildlife` directory of this repostory.
3. Copy the downloaded configuration files into your local repository of [mmdetection](https://github.com/open-mmlab/mmdetection "mmdetection") and its `mmdetection/configs/african-wildlife` directory.
4. Copy the downloaded weights into your local repository of [mmdetection](https://github.com/open-mmlab/mmdetection "mmdetection") and its `work_dirs` directory.
5. Run the following command:
```bash
python tools/test.py configs/african-wildlife/<CONFIG_NAME> work_dirs/<MODEL_NAME>/epoch_100.pth
```
6. Copy the results from your terminal and paste them into the blank spaces under each model name in this README.

### Sample Model
```
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.196
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=1000 ] = 0.427
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=1000 ] = 0.144
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=1000 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=1000 ] = 0.183
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=1000 ] = 0.207
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.524
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=300 ] = 0.524
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=1000 ] = 0.524
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=1000 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=1000 ] = 0.416
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=1000 ] = 0.544
04/15 16:26:11 - mmengine - INFO - bbox_mAP_copypaste: 0.196 0.427 0.144 0.000 0.183 0.207
04/15 16:26:11 - mmengine - INFO - Epoch(test) [225/225]    coco/bbox_mAP: 0.1960  coco/bbox_mAP_50: 0.4270  coco/bbox_mAP_75: 0.1440  coco/bbox_mAP_s: 0.0000  coco/bbox_mAP_m: 0.1830  coco/bbox_mAP_l: 0.2070  data_time: 0.0143  time: 0.1402
```

### YOLOv8
Since YOLOv8 is not a part of mmdetection, the format will be different. Post the mAP scores, how long it took to inference each image, and if possible, the memory usage during inferencing.
```
<PASTE YOUR RESULTS HERE>
```

### Faster R-CNN
Configuration file: `configs/african-wildlife/faster-rcnn_r50_fpn.py`
```
04/21 11:26:42 - mmengine - INFO - Load checkpoint from work_dirs/faster-rcnn_r50_fpn/epoch_100.pth
04/21 11:26:48 - mmengine - INFO - Epoch(test) [ 50/225]    eta: 0:00:21  time: 0.1229  data_time: 0.0858  memory: 351
04/21 11:26:49 - mmengine - INFO - Epoch(test) [100/225]    eta: 0:00:08  time: 0.0189  data_time: 0.0003  memory: 366
04/21 11:26:50 - mmengine - INFO - Epoch(test) [150/225]    eta: 0:00:04  time: 0.0189  data_time: 0.0004  memory: 366
04/21 11:26:51 - mmengine - INFO - Epoch(test) [200/225]    eta: 0:00:01  time: 0.0184  data_time: 0.0004  memory: 366
04/21 11:26:51 - mmengine - INFO - Evaluating bbox...
Loading and preparing results...
DONE (t=0.00s)
creating index...
index created!
Running per image evaluation...
Evaluate annotation type *bbox*
DONE (t=0.05s).
Accumulating evaluation results...
DONE (t=0.02s).
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.643
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=1000 ] = 0.891
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=1000 ] = 0.717
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=1000 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=1000 ] = 0.468
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=1000 ] = 0.672
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.708
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=300 ] = 0.708
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=1000 ] = 0.708
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=1000 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=1000 ] = 0.530
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=1000 ] = 0.736
04/21 11:26:51 - mmengine - INFO - bbox_mAP_copypaste: 0.643 0.891 0.717 0.000 0.468 0.672
04/21 11:26:51 - mmengine - INFO - Epoch(test) [225/225]    coco/bbox_mAP: 0.6430  coco/bbox_mAP_50: 0.8910  coco/bbox_mAP_75: 0.7170  coco/bbox_mAP_s: 0.0000  coco/bbox_mAP_m: 0.4680  coco/bbox_mAP_l: 0.6720  data_time: 0.0194  time: 0.0419
```

### RTMDET
Configuration file: `configs/african-wildlife/rtmdet_l_8xb32-300e_coco.py`
```
04/21 11:28:46 - mmengine - INFO - Epoch(test) [ 50/225]    eta: 0:00:21  time: 0.1235  data_time: 0.0844  memory: 598
04/21 11:28:47 - mmengine - INFO - Epoch(test) [100/225]    eta: 0:00:09  time: 0.0271  data_time: 0.0004  memory: 598
04/21 11:28:48 - mmengine - INFO - Epoch(test) [150/225]    eta: 0:00:04  time: 0.0271  data_time: 0.0005  memory: 598
04/21 11:28:50 - mmengine - INFO - Epoch(test) [200/225]    eta: 0:00:01  time: 0.0269  data_time: 0.0005  memory: 598
04/21 11:28:51 - mmengine - INFO - Evaluating bbox...
Loading and preparing results...
DONE (t=0.11s)
creating index...
index created!
Running per image evaluation...
Evaluate annotation type *bbox*
DONE (t=0.64s).
Accumulating evaluation results...
DONE (t=0.28s).
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.713
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.914
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.794
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.238
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.568
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.738
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.516
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.782
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.800
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.250
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.685
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.818
04/21 11:28:52 - mmengine - INFO - bbox_mAP_copypaste: 0.713 0.914 0.794 0.238 0.568 0.738
04/21 11:28:52 - mmengine - INFO - Epoch(test) [225/225]    coco/bbox_mAP: 0.7130  coco/bbox_mAP_50: 0.9140  coco/bbox_mAP_75: 0.7940  coco/bbox_mAP_s: 0.2380  coco/bbox_mAP_m: 0.5680  coco/bbox_mAP_l: 0.7380  data_time: 0.0191  time: 0.0484
```

### DINO
Configuration file: `configs/african-wildlife/dino-5scale_swin-l_8xb2-12e_coco.py`
```
04/21 11:31:10 - mmengine - INFO - Epoch(test) [ 50/225]    eta: 0:00:22  time: 0.1295  data_time: 0.0446  memory: 1198

04/21 11:31:13 - mmengine - INFO - Epoch(test) [100/225]    eta: 0:00:12  time: 0.0699  data_time: 0.0005  memory: 1312

04/21 11:31:17 - mmengine - INFO - Epoch(test) [150/225]    eta: 0:00:06  time: 0.0681  data_time: 0.0006  memory: 1312

04/21 11:31:20 - mmengine - INFO - Epoch(test) [200/225]    eta: 0:00:02  time: 0.0703  data_time: 0.0006  memory: 1312

04/21 11:31:23 - mmengine - INFO - Evaluating bbox...
Loading and preparing results...
DONE (t=0.11s)
creating index...
index created!
Running per image evaluation...
Evaluate annotation type *bbox*
DONE (t=1.11s).
Accumulating evaluation results...
DONE (t=0.61s).
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.788
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=1000 ] = 0.930
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=1000 ] = 0.843
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=1000 ] = 0.118
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=1000 ] = 0.607
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=1000 ] = 0.817
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.873
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=300 ] = 0.883
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=1000 ] = 0.883
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=1000 ] = 0.117
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=1000 ] = 0.782
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=1000 ] = 0.905
04/21 11:31:25 - mmengine - INFO - bbox_mAP_copypaste: 0.788 0.930 0.843 0.118 0.607 0.817
04/21 11:31:25 - mmengine - INFO - Epoch(test) [225/225]    coco/bbox_mAP: 0.7880  coco/bbox_mAP_50: 0.9300  coco/bbox_mAP_75: 0.8430  coco/bbox_mAP_s: 0.1180  coco/bbox_mAP_m: 0.6070  coco/bbox_mAP_l: 0.8170  data_time: 0.0103  time: 0.0829
```

---

## Bounding Box Visuals
This section will detail how to obtain the bounding box predictions on a provided sample image. Follow these steps:

1. Download the [weights of the models](https://o365coloradoedu-my.sharepoint.com/:f:/g/personal/jung5864_colorado_edu/EuUUd68bKmVIjZiH52WXiRIBtcMcpPFJhK_UaK0vUjXAGQ?e=EeW5mr) trained by Justin.
2. Download the configuration files in the `mmdetection/configs/african-wildlife` directory of this repostory.
3. Copy the downloaded configuration files into your local repository of [mmdetection](https://github.com/open-mmlab/mmdetection "mmdetection") and its `mmdetection/configs/african-wildlife` directory.
4. Copy the downloaded weights into your local repository of [mmdetection](https://github.com/open-mmlab/mmdetection "mmdetection") and its `work_dirs` directory.
5. Copy the images in the `images` directory of this repository to the `demo` directory of your local repository of [mmdetection](https://github.com/open-mmlab/mmdetection "mmdetection")
6. Run the following command:
```bash
python demo/image_demo.py demo/<IMAGE NAME> configs/african-wildlife/<CONFIG_NAME> --weights work_dirs/<MODEL_NAME>/epoch_100.pth
```
7. Upload the resulting visuals to this repository

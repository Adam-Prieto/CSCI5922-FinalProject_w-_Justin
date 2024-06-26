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

### YOLOv8 Nano
Since YOLOv8 is not a part of mmdetection, the format will be different. Post the mAP scores, how long it took to inference each image, and if possible, the memory usage during inferencing.
```
YOLOv8n summary (fused): 168 layers, 3006428 parameters, 0 gradients, 8.1 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 225/225 [00:
                   all        225        379      0.889      0.838      0.911        0.7
               buffalo        225         89      0.949      0.876      0.945      0.749
              elephant        225         91      0.726      0.813      0.863      0.638
                 rhino        225         85      0.952      0.847      0.922      0.753
                 zebra        225        114      0.928      0.816      0.912      0.662
Speed: 0.2ms preprocess, 8.9ms inference, 0.0ms loss, 3.9ms postprocess per image

---
Memory usage during inferencing: 802 MiB
```

### YOLOv8 Medium
Since YOLOv8 is not a part of mmdetection, the format will be different. Post the mAP scores, how long it took to inference each image, and if possible, the memory usage during inferencing.
```
YOLOv8m summary (fused): 218 layers, 25842076 parameters, 0 gradients, 78.7 GFLOPs
                 Class     Images  Instances      Box(P          R      mAP50  mAP50-95): 100%|██████████| 225/225 [00:
                   all        225        379      0.929      0.813      0.916      0.748
               buffalo        225         89       0.96      0.813      0.935      0.777
              elephant        225         91      0.869      0.791      0.875      0.697
                 rhino        225         85       0.96      0.852      0.947       0.81
                 zebra        225        114      0.928      0.795      0.906      0.708
Speed: 0.2ms preprocess, 10.7ms inference, 0.0ms loss, 3.7ms postprocess per image

---
Memory usage during inferencing: 984 MiB
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

```
04/22 21:19:49 - mmengine - INFO - before build:
04/22 21:19:49 - mmengine - INFO - (GB) mem_used: 17.65 | uss: 0.23 | total_proc: 1
Loads checkpoint by local backend from path: work_dirs/faster-rcnn_r50_fpn/epoch_100.pth
loading annotations into memory...
Done (t=0.00s)
creating index...
index created!
04/22 21:19:50 - mmengine - INFO - after build:
04/22 21:19:50 - mmengine - INFO - (GB) mem_used: 17.83 | uss: 0.38 | total_proc: 1
04/22 21:19:52 - mmengine - INFO - ==================================
04/22 21:19:52 - mmengine - INFO - Done image [50 /2000], fps: 56.9 img/s, times per image: 17.6 ms/img, cuda memory: 351 MB
04/22 21:19:53 - mmengine - INFO - (GB) mem_used: 19.80 | uss: 2.11 | total_proc: 1
04/22 21:19:54 - mmengine - INFO - ==================================
04/22 21:19:54 - mmengine - INFO - Done image [100/2000], fps: 56.9 img/s, times per image: 17.6 ms/img, cuda memory: 366 MB
04/22 21:19:54 - mmengine - INFO - (GB) mem_used: 19.80 | uss: 2.11 | total_proc: 1
04/22 21:19:55 - mmengine - INFO - ==================================
04/22 21:19:55 - mmengine - INFO - Done image [150/2000], fps: 57.0 img/s, times per image: 17.5 ms/img, cuda memory: 366 MB
04/22 21:19:55 - mmengine - INFO - (GB) mem_used: 19.80 | uss: 2.11 | total_proc: 1
04/22 21:19:56 - mmengine - INFO - ==================================
04/22 21:19:56 - mmengine - INFO - Done image [200/2000], fps: 57.3 img/s, times per image: 17.5 ms/img, cuda memory: 366 MB
04/22 21:19:56 - mmengine - INFO - (GB) mem_used: 19.79 | uss: 2.11 | total_proc: 1
04/22 21:19:56 - mmengine - INFO - ============== Done ==================
04/22 21:19:56 - mmengine - INFO - Overall fps: 57.3 img/s, times per image: 17.5 ms/img
04/22 21:19:56 - mmengine - INFO - cuda memory: 366 MB
04/22 21:19:56 - mmengine - INFO - (GB) mem_used: 19.80 | uss: 2.11 | total_proc: 1
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

```
04/22 21:23:57 - mmengine - INFO - before build:
04/22 21:23:57 - mmengine - INFO - (GB) mem_used: 17.70 | uss: 0.23 | total_proc: 1
Loads checkpoint by local backend from path: work_dirs/rtmdet_l_8xb32-300e_coco/epoch_100.pth
loading annotations into memory...
Done (t=0.00s)
creating index...
index created!
04/22 21:23:58 - mmengine - INFO - after build:
04/22 21:23:58 - mmengine - INFO - (GB) mem_used: 17.86 | uss: 0.38 | total_proc: 1
04/22 21:24:01 - mmengine - INFO - ==================================
04/22 21:24:01 - mmengine - INFO - Done image [50 /2000], fps: 32.6 img/s, times per image: 30.7 ms/img, cuda memory: 397 MB
04/22 21:24:01 - mmengine - INFO - (GB) mem_used: 19.84 | uss: 2.11 | total_proc: 1
04/22 21:24:03 - mmengine - INFO - ==================================
04/22 21:24:03 - mmengine - INFO - Done image [100/2000], fps: 32.5 img/s, times per image: 30.8 ms/img, cuda memory: 397 MB
04/22 21:24:03 - mmengine - INFO - (GB) mem_used: 19.86 | uss: 2.11 | total_proc: 1
04/22 21:24:05 - mmengine - INFO - ==================================
04/22 21:24:05 - mmengine - INFO - Done image [150/2000], fps: 32.2 img/s, times per image: 31.0 ms/img, cuda memory: 397 MB
04/22 21:24:05 - mmengine - INFO - (GB) mem_used: 19.85 | uss: 2.11 | total_proc: 1
04/22 21:24:07 - mmengine - INFO - ==================================
04/22 21:24:07 - mmengine - INFO - Done image [200/2000], fps: 32.2 img/s, times per image: 31.1 ms/img, cuda memory: 397 MB
04/22 21:24:07 - mmengine - INFO - (GB) mem_used: 19.85 | uss: 2.11 | total_proc: 1
04/22 21:24:08 - mmengine - INFO - ============== Done ==================
04/22 21:24:08 - mmengine - INFO - Overall fps: 32.2 img/s, times per image: 31.1 ms/img
04/22 21:24:08 - mmengine - INFO - cuda memory: 397 MB
04/22 21:24:08 - mmengine - INFO - (GB) mem_used: 19.85 | uss: 2.11 | total_proc: 1
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

```
04/22 21:27:39 - mmengine - INFO - before build:
04/22 21:27:39 - mmengine - INFO - (GB) mem_used: 17.65 | uss: 0.23 | total_proc: 1
Loads checkpoint by local backend from path: work_dirs/dino-5scale_swin-l_8xb2-12e_coco/epoch_36.pth
loading annotations into memory...
Done (t=0.00s)
creating index...
index created!
04/22 21:27:42 - mmengine - INFO - after build:
04/22 21:27:42 - mmengine - INFO - (GB) mem_used: 17.81 | uss: 0.38 | total_proc: 1
04/22 21:27:47 - mmengine - INFO - ==================================
04/22 21:27:47 - mmengine - INFO - Done image [50 /2000], fps: 13.8 img/s, times per image: 72.6 ms/img, cuda memory: 1198 MB
04/22 21:27:47 - mmengine - INFO - (GB) mem_used: 19.84 | uss: 2.11 | total_proc: 1
04/22 21:27:50 - mmengine - INFO - ==================================
04/22 21:27:50 - mmengine - INFO - Done image [100/2000], fps: 14.8 img/s, times per image: 67.4 ms/img, cuda memory: 1312 MB
04/22 21:27:50 - mmengine - INFO - (GB) mem_used: 19.81 | uss: 2.11 | total_proc: 1
04/22 21:27:53 - mmengine - INFO - ==================================
04/22 21:27:53 - mmengine - INFO - Done image [150/2000], fps: 15.4 img/s, times per image: 64.9 ms/img, cuda memory: 1312 MB
04/22 21:27:53 - mmengine - INFO - (GB) mem_used: 19.73 | uss: 2.11 | total_proc: 1
04/22 21:27:57 - mmengine - INFO - ==================================
04/22 21:27:57 - mmengine - INFO - Done image [200/2000], fps: 15.6 img/s, times per image: 64.1 ms/img, cuda memory: 1312 MB
04/22 21:27:57 - mmengine - INFO - (GB) mem_used: 19.81 | uss: 2.11 | total_proc: 1
04/22 21:27:58 - mmengine - INFO - ============== Done ==================
04/22 21:27:58 - mmengine - INFO - Overall fps: 15.6 img/s, times per image: 64.1 ms/img
04/22 21:27:58 - mmengine - INFO - cuda memory: 1312 MB
04/22 21:27:58 - mmengine - INFO - (GB) mem_used: 19.81 | uss: 2.11 | total_proc: 1
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

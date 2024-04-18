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
<PASTE YOUR RESULTS HERE>
```

### RTMDET
Configuration file: `configs/african-wildlife/rtmdet_l_8xb32-300e_coco.py`
```
<PASTE YOUR RESULTS HERE>
```

### DINO
Configuration file: `configs/african-wildlife/dino-5scale_swin-l_8xb2-12e_coco.py`
```
<PASTE YOUR RESULTS HERE>
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

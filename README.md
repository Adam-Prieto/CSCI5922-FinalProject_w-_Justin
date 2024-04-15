# CSCI5922-FinalProject_w-_Justin

## Updates (As they occur)

4/12 - Fully trained YoloV8 model on African Animal dataset after much headache. My next step is to get this model working with others from the google doc page. Also, training
the model on 100 epoch took a lot longer than I would've guessed. Would not recommend.

4/14 
* More models are located [here](https://github.com/open-mmlab/mmdetection?tab=readme-ov-file#overview-of-benchmark-and-model-zoo).
* Loading models with mmdet runs into an installation error: NotImplementedError: A UTF-8 locale is required. Got ANSI_X3.4-1968. This error severly impacts loading pretrained models into google colab.
* [Link](https://github.com/open-mmlab/mmdetection/tree/main/configs/rtmdet) tries to work through installation, looking into now. 

## Put results from the Object Detection section here

### [1.) mmdetection](https://github.com/open-mmlab/mmdetection/tree/main/configs/fast_rcnn)
* Code base is confusing and doesn't offer pretrained models.
* Recommend to stay away from.


### [2.) Faster R-CNN](https://github.com/open-mmlab/mmdetection/tree/main/configs/faster_rcnn)
* No code provided.


## Convert YOLO dataset to COCO format
```
from pathlib import Path

import globox


def main():
  folder = Path("datasets/african-wildlife/valid/labels/")  # Where the .txt files are
  image_folder = Path("datasets/african-wildlife/valid/images/")
  save_file = Path("annotation_coco.json")

  annotations = globox.AnnotationSet.from_yolo_v5(folder=folder, image_folder=image_folder)
  annotations.show_stats()
  annotations.save_coco(save_file, auto_ids=True)


if __name__ == "__main__":
    main()
```
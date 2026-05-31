# Week 3 Task 2 - Video Comparison using YOLO and FFmpeg

## Objective

Create a comparison video consisting of:

1. Raw Video
2. Object Detection Video
3. Object Segmentation Video

stacked vertically using FFmpeg.

## Tools Used

* Google Colab
* Python
* OpenCV
* Ultralytics YOLOv8
* FFmpeg
* MoviePy

## Workflow

1. Downloaded video from YouTube.
2. Extracted frames.
3. Performed Object Detection using YOLOv8.
4. Performed Object Segmentation using YOLOv8-Seg.
5. Generated detection and segmentation videos.
6. Resized all videos to identical dimensions.
7. Used FFmpeg vstack to combine videos vertically.
8. Removed original audio.
9. Added a new soundtrack.
10. Generated final comparison video.

## Output Layout

Top: Raw Video

Middle: Object Detection

Bottom: Object Segmentation

## Result

Successfully created a stacked comparison video showing the differences between raw video, object detection, and object segmentation outputs.

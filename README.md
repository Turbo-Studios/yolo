# YOLO v10

YOLO v10 implementation.

## Installation

`conda` virtual environment is recommended. 

### Download and Install

⚠️ The 2nd line is for **NVIDIA** Graphic Cards only!
```
pip install  supervision labelme   labelme2yolo huggingface_hub  google_cloud_audit_log`

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

pip install  git+https://github.com/THU-MIG/yolov10.git
```

Then, download the models from the [release page](https://github.com/Turbo-Studios/yolo/releases) to your project folder.

### Summary

The correct project folder should be in the structure like:

```
yolov10
 ├─ gen_imgs.py
 ├─ yolov10-detect.py
 ├─ yolov10-infer.py
 ├─ yolov10b.onnx
 ├─ yolov10b.py
 ├─ yolov10l.onnx
 ├─ yolov10l.py
 ├─ yolov10m.onnx
 ├─ yolov10m.py
 ├─ yolov10n.onnx
 ├─ yolov10n.py
 ├─ yolov10s.onnx
 ├─ yolov10s.py
 ├─ yolov10x.onnx
 └─ yolov10x.py
```

## Use

`yolov10-infer.py` will call your system's web camera and start a session.

`gen_imgs.py` can capture your camera screen when `S` is pressed. The captured picture can be used to train your model after labeling.

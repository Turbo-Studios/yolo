# YOLO v10

YOLO v10 implementation.

## Installation

`conda` virtual environment is recommended. 

⚠️ The 2nd line is for **NVIDIA** Graphic Cards only!
```
pip install  supervision labelme   labelme2yolo huggingface_hub  google_cloud_audit_log`

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

pip install  git+https://github.com/THU-MIG/yolov10.git
```

Then, download the models from the [release page](https://github.com/Turbo-Studios/yolo/releases) to your project folder.

## Use

`yolov10-infer.py` will call your system's web camera and start a session.

`gen_imgs.py` can capture your camera screen when `S` is pressed. The captured picture can be used to train your model after labeling.

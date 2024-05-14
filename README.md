# Synchronized Object Detection for Autonomous Sorting, Mapping, and Quantification of Medical Materials
This repository contains the code, the dataset, and the demo videos of the paper: Zocco, F., Lake, D., and Rahimifard, S., 2024. Synchronized object detection for autonomous sorting, mapping, and quantification of medical materials. arXiv preprint arXiv:2405.06821.

## Description of Folders
### Demo Videos
The 2 demo videos are inside the folder "Demo_videos". To respect the file size limit of GitHub, they have been split into parts. Specifically, Demo1 is made of 2 parts, whereas Demo2 is made of 7 parts. The parts can be merged into a single video using one of the many tools available. 

Demo1 shows the real-time detection of inhalers, whereas Demo2 shows the real-time synchromaterials.


### Dataset
To respect the file size limit of GitHub, the dataset 5IPP has been split into 4 parts. To prepare 5IPP for use, follow the instructions given in: Dataset => 5IPP => JPEGImages => ReadMe.txt.


### Code 
How to use the code:
1. Set the static IP addresses of the laptop and the 2 Jetson Nanos 
2. Connect laptop and both Jetson Nanos to the Netgear network switch using Ethernet cables (3 cables in total)
3. Each Jetson Nano is connected to a camera, a mouse, a keyboard, a power supply, an Ethernet cable, and a monitor
4. On the laptop, run “receiver_v9.py”
5. On the Terminal of each Nano, run:
* cd jetson-inference
* python detectnet-mmu_v3.py --model=python/training/detection/ssd/models/5IPPnet/ssd-mobilenet.onnx --labels=python/training/detection/ssd/models/5IPPnet/labels.txt --input-blob=input_0 --output-cvg=scores -- 
      output-bbox=boxes /dev/video0 

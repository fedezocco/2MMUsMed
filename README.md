# Synchronized Object Detection for Autonomous Sorting, Mapping, and Quantification of Materials in Circular Healthcare
This repository contains the code, the dataset, and the demo videos of the paper: Zocco, F., Lake, D.R., McLoone, S. and Rahimifard, S., 2025. Synchronized object detection for autonomous sorting, mapping, and quantification of materials in circular healthcare. arXiv preprint arXiv:2405.06821.

![summaryFig](https://github.com/fedezocco/2MMUsMed/assets/62107909/bb653cc4-33ea-49de-9436-84ded12b9559)


## Description of Folders
### Demo Videos
The 2 demo videos are inside the folder "Demo_videos". To respect the file size limit of GitHub, they have been split into parts. Specifically, Demo1 is made of 2 parts, whereas Demo2 is made of 7 parts. The parts can be merged into a single video using one of the many tools available. 

Demo1 shows the real-time detection of inhalers, whereas Demo2 shows the real-time synchromaterials.


### Dataset
To respect the file size limit of GitHub, the dataset 5IPP has been split into 4 parts. To prepare 5IPP for use:
1. Unzip 5IPP folder and use the unzipped 5IPP as the dataset folder
2. Follow the instructions given in: 5IPP (unzipped) => JPEGImages => ReadMe.txt.


### Code 
How to use the code:
1. Set the static IP addresses of the laptop and the 2 Jetson Nanos 
2. Connect laptop and both Jetson Nanos to the Netgear network switch using Ethernet cables (3 cables in total)
3. Each Jetson Nano is connected to a camera, a mouse, a keyboard, a power supply, an Ethernet cable, and a monitor
4. On the laptop, run “receiver_v9.py”
5. On the command prompt of each Nano, run:
* cd jetson-inference
* python detectnet-mmu_v3.py --model=python/training/detection/ssd/models/5IPPnet/ssd-mobilenet.onnx --labels=python/training/detection/ssd/models/5IPPnet/labels.txt --input-blob=input_0 --output-cvg=scores -- 
      output-bbox=boxes /dev/video0 

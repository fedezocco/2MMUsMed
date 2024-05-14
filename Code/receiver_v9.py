"""Implemented by Federico Zocco
    Last update: 14 May 2024
        
    Script to be run on the material data concentrator [1]. This
    version works with 2 units, but it can be adapted to
    work with more units.  
    
    References:
        [1] Zocco, F., Lake, D., and Rahimifard, S., 2024. 
        Synchronized object detection for autonomous sorting, mapping, 
        and quantification of medical materials. arXiv preprint arXiv:2405.06821.
        [2] Question on Stack Overflow: 
        https://stackoverflow.com/questions/60924037/udp-using-ethernet-cable-point-to-point-communication-is-not-working
"""


import socket
import numpy as np
import matplotlib.pyplot as plt
import time
from add_up_materials_v2 import add_up_materials
from operator import add


# Communication settings:
UDP_IP="IP of receiver" #e.g.: UDP_IP="192.168.0.191"   
UDP_PORT="same port for all devices" #e.g.: UDP_PORT=2000 
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
##################

# IDs of units:
number_of_units = 2
unit_ids = list(range(1,number_of_units+1))
    
same_time_window = 0.5 # (in seconds) it will be added up the materials of detections within "same_time_window" 
detections_allUnits = [] 


maxClassId = 20 # highest ID of a class
ids_of_classes = list(range(0, maxClassId))      

    
# Prepare live bar charts:
fig = plt.figure()
fig.set_size_inches(20, 20)
ax1 = fig.add_subplot(2,2,3) # plot for unit 1
ax2 = fig.add_subplot(2,2,4) # plot for unit 2
ax3 = fig.add_subplot(2,1,1) # plot for unit 1 + unit 2 
material_ids = [1,2,3,4] # 1: rubber; 2: plastic; 3: paper; 4: metal
current_masses_u1 = [0,0,0,0] 
current_masses_u2 = [0,0,0,0]
current_sum_AllUnits = list(map(add, current_masses_u1, current_masses_u2))     


# Initialize bar charts with no masses:
ax1.bar(material_ids, [0,0,0,0], color='blue')
ax1.set_xticks(material_ids)
ax1.set_xticklabels(['rubber', 'plastic', 'paper', 'metal'], fontdict=None, minor=False)
ax1.set_ylabel('Mass (gram)')
ax1.set_title('From Unit 1')
ax2.bar(material_ids, [0,0,0,0], color='orange')
ax2.set_xticks(material_ids)
ax2.set_xticklabels(['rubber', 'plastic', 'paper', 'metal'], fontdict=None, minor=False)
ax2.set_ylabel('Mass (gram)')
ax2.set_title('From Unit 2')
ax3.bar(material_ids, [0,0,0,0], color='black')
ax3.set_xticks(material_ids)
ax3.set_xticklabels(['rubber', 'plastic', 'paper', 'metal'], fontdict=None, minor=False)
ax3.set_ylabel('Mass (gram)')
ax3.set_title('Unit 1 + Unit 2')
fig.suptitle('Synchromaterials')
plt.show(block=False)
plt.pause(0.5)
    
start = time.clock()

while True: 
    
    # Read data from ethernet port:
    mmu_data_str, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    ###############
    mmu_data_str = mmu_data_str.decode('utf-8') # convert string to array
    mmu_data = np.array(np.matrix(mmu_data_str)).ravel() # convert string to array
    
    print("mmu_data", mmu_data)
    # input vector from a unit: 
    # [unitId, detection_1, ..., detection_N]
    
    current_unit_id = mmu_data[0]
    current_detection = mmu_data[1:None]
    print("current_detection", current_detection)
    detections_allUnits = detections_allUnits + list(current_detection)
    
    
    if current_unit_id == unit_ids[0]: # detection from unit 1 
        
        ax1.cla() # clear axes before updating
        ax2.cla() # clear axes before updating
        ax3.cla() # clear axes before updating
    
        current_masses_u1 = add_up_materials(current_detection, material_ids)
        ax1.bar(material_ids, current_masses_u1, color='blue')
        ax1.set_xticks(material_ids)
        ax1.set_xticklabels(['rubber', 'plastic', 'paper', 'metal'], fontdict=None, minor=False)
        ax1.set_ylabel('Mass (gram)')
        ax1.set_title('From Unit 1')
        ax2.bar(material_ids, current_masses_u2, color='orange')
        ax2.set_xticks(material_ids)
        ax2.set_xticklabels(['rubber', 'plastic', 'paper', 'metal'], fontdict=None, minor=False)
        ax2.set_ylabel('Mass (gram)')
        ax2.set_title('From Unit 2')
        ax3.bar(material_ids, current_sum_AllUnits, color='black')
        ax3.set_xticks(material_ids)
        ax3.set_xticklabels(['rubber', 'plastic', 'paper', 'metal'], fontdict=None, minor=False)
        ax3.set_ylabel('Mass (gram)')
        ax3.set_title('Unit 1 + Unit 2')
        fig.suptitle('Synchromaterials')
        
    
    elif current_unit_id == unit_ids[1]: # detection from unit 2 
        
        ax1.cla() 
        ax2.cla() 
        ax3.cla() 
    
        current_masses_u2 = add_up_materials(current_detection, material_ids)
        ax1.bar(material_ids, current_masses_u1, color='blue')
        ax1.set_xticks(material_ids)
        ax1.set_xticklabels(['rubber', 'plastic', 'paper', 'metal'], fontdict=None, minor=False)
        ax1.set_ylabel('Mass (gram)')
        ax1.set_title('From Unit 1')
        ax2.bar(material_ids, current_masses_u2, color='orange')
        ax2.set_xticks(material_ids)
        ax2.set_xticklabels(['rubber', 'plastic', 'paper', 'metal'], fontdict=None, minor=False)
        ax2.set_ylabel('Mass (gram)')
        ax2.set_title('From Unit 2')
        ax3.bar(material_ids, current_sum_AllUnits, color='black')
        ax3.set_xticks(material_ids)
        ax3.set_xticklabels(['rubber', 'plastic', 'paper', 'metal'], fontdict=None, minor=False)
        ax3.set_ylabel('Mass (gram)')
        ax3.set_title('Unit 1 + Unit 2')
        fig.suptitle('Synchromaterials')
    
    elapsed = (time.clock() - start)
    if elapsed >= same_time_window:
        print("detections_allUnits with repetitions", detections_allUnits)
        detections_allUnits = list(dict.fromkeys(detections_allUnits))
        print("detections_allUnits", detections_allUnits)
        current_sum_AllUnits = add_up_materials(detections_allUnits, material_ids) 
        detections_allUnits = [] # reset detected classes for next same-time window
        start = time.clock() # reset clock for next same-time window
        
    plt.show(block=False)
    plt.pause(0.15)
    
    
    




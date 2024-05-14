"""Implemented by Federico Zocco
    Last update: 14 May 2024
        
    Script called by "receiver_v9.py" to add-up the masses of materials detected
    by one or more units in the system. The result is displayed by the material
    data concentrator [1]. 
    
    References:
        [1] Zocco, F., Lake, D., and Rahimifard, S., 2024. 
        Synchronized object detection for autonomous sorting, mapping, 
        and quantification of medical materials. arXiv preprint arXiv:2405.06821.
"""


import numpy as np
from operator import add
from classToMasses_v2 import classToMasses

def add_up_materials(detected_classes, material_ids): 
    
    material_masses = np.zeros((len(material_ids)))
    
    for i in detected_classes:
        material_masses = list(map(add, material_masses, classToMasses(i)))  
        
    return material_masses 
"""Implemented by Federico Zocco
    Last update: 14 May 2024
        
    Script called by "add_up_materials_v2.py" to convert the detected classes of
    objects into masses expressed in grams [1]. 
    
    References:
        [1] Zocco, F., Lake, D., and Rahimifard, S., 2024. 
        Synchronized object detection for autonomous sorting, mapping, 
        and quantification of medical materials. arXiv preprint arXiv:2405.06821.
"""


def classToMasses(current_detection): 
    
    if 0 <= current_detection <= 2:
        masses = [0.5, 0, 0, 0] # in grams
    elif current_detection == 3:
        masses = [0, 0.5, 0, 0] # in grams
    elif 4 <= current_detection <= 5:
        masses = [0, 0, 0.5, 0] # in grams
    else: 
        masses = [0, 0, 0, 0.5] # in grams
        
    return masses 
        

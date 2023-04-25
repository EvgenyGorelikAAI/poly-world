from scipy.spatial.transform import Rotation
import numpy as np

def array_from_dict(params: dict):
    h       = params.get("h", 0) 
    w       = params.get("w", 0) 
    l       = params.get("l", 0) 
    x       = params.get("x", 0) 
    y       = params.get("y", 0) 
    z       = params.get("z", 0) 
    roll    = params.get("roll", 0)
    pitch   = params.get("pitch", 0)
    yaw     = params.get("yaw", 0)
    return np.array([x,y,z,roll,pitch,yaw,l,w,h])

def bbox2reference(bbox, reference):
    nbbox = bbox.copy()
    nbbox[:3] = Rotation.from_euler("xyz",reference[3:6], degrees=False).inv().apply(bbox[:3] - reference[:3])
    nbbox[3:6] -= reference[3:6]
    return nbbox
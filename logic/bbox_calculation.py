from scipy.spatial.transform import Rotation
import numpy as np
from typing import Union

def bbox_corners(bbox: Union[dict, np.ndarray]):
    """
        Return : 3xn 
        Reference: https://github.com/yeyang1021/KITTI_VIZ_3D/blob/master/kitti_util.py
    """
    if isinstance(bbox, dict):
        h       = bbox.get("h", 0) 
        w       = bbox.get("w", 0) 
        l       = bbox.get("l", 0) 
        x       = bbox.get("x", 0) 
        y       = bbox.get("y", 0) 
        z       = bbox.get("z", 0) 
        roll    = bbox.get("roll", 0)
        pitch   = bbox.get("pitch", 0)
        yaw     = bbox.get("yaw", 0)
    elif isinstance(bbox, np.ndarray):
        assert bbox.shape == (9,)
        x       = bbox[0] 
        y       = bbox[1] 
        z       = bbox[2] 
        roll    = bbox[3]
        pitch   = bbox[4]
        yaw     = bbox[5]
        l       = bbox[6] 
        w       = bbox[7] 
        h       = bbox[8]
    else:
        raise NotImplementedError("Bounding Box type not implemented")
    R = Rotation.from_euler("xyz", [roll, pitch, yaw], degrees=False).as_matrix()
    corners = np.array([    [l/2,l/2,-l/2,-l/2,l/2,l/2,-l/2,-l/2],
                            [w/2,-w/2,-w/2,w/2,w/2,-w/2,-w/2,w/2],
                            [0,0,0,0,h,h,h,h]])
    corners = R @ corners
    corners += np.vstack([x, y, z])
    return corners
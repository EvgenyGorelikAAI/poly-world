from typing import Union
import numpy as np
from scipy.spatial.transform import Rotation
from scipy.spatial import ConvexHull
from .polygon import Polygon

class BoundingBox(Polygon):
    def __init__(self, bbox: Union[dict, np.ndarray]) -> None:
        super().__init__()
        """
            Return : 3xn 
            Reference: https://github.com/yeyang1021/KITTI_VIZ_3D/blob/master/kitti_util.py
        """
        if isinstance(bbox, dict):
            self.h       = bbox.get("h", 0) 
            self.w       = bbox.get("w", 0) 
            self.l       = bbox.get("l", 0) 
            self.x       = bbox.get("x", 0) 
            self.y       = bbox.get("y", 0) 
            self.z       = bbox.get("z", 0) 
            self.roll    = bbox.get("roll", 0)
            self.pitch   = bbox.get("pitch", 0)
            self.yaw     = bbox.get("yaw", 0)
        elif isinstance(bbox, np.ndarray):
            assert bbox.shape == (9,)
            self.x       = bbox[0] 
            self.y       = bbox[1] 
            self.z       = bbox[2] 
            self.roll    = bbox[3]
            self.pitch   = bbox[4]
            self.yaw     = bbox[5]
            self.l       = bbox[6] 
            self.w       = bbox[7] 
            self.h       = bbox[8]
        else:
            raise NotImplementedError("Bounding Box type not implemented")
        self.corners = self.get_corners()
        self.A, self.b = self.constraints(self.corners)

    def get_corners(self):
        R = Rotation.from_euler("xyz", [self.roll, self.pitch, self.yaw], degrees=False).as_matrix()
        corners = np.array([    [self.l/2,self.l/2,-self.l/2,-self.l/2,self.l/2,self.l/2,-self.l/2,-self.l/2],
                                [self.w/2,-self.w/2,-self.w/2,self.w/2,self.w/2,-self.w/2,-self.w/2,self.w/2],
                                [0,0,0,0,self.h,self.h,self.h,self.h]])
        corners = R @ corners
        corners += np.vstack([self.x, self.y, self.z])
        return corners


    def constraints(self, corners):
        hull = ConvexHull(corners).equations.T
        A, b = hull[:-1], hull[-1]
        return A, b

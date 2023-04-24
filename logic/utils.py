import numpy as np

def spherical2cartesian(radius, azimuth, elevation):
    '''
        Reference https://keisan.casio.com/exec/system/1359534351
    '''
    x = radius * np.sin(elevation) * np.cos(azimuth)
    y = radius * np.sin(elevation) * np.sin(azimuth)
    z = radius * np.cos(elevation)
    return np.stack([x,y,z]).T
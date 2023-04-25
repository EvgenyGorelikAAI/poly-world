from scipy.spatial import ConvexHull
import numpy as np

def snap_close_values(vec1, vec2, epsilon=1e-6):
    close_idx = np.linalg.norm(vec1.reshape(1,-1) - vec2.reshape(1,-1), axis=0) < epsilon
    vec1[close_idx] = vec2[close_idx]
    return vec1 

def calc_hit(ray: np.ndarray, convex_hull: ConvexHull):
    '''
        oriented and debugged implementation from reference: 
        https://stackoverflow.com/questions/30486312/intersection-of-nd-line-with-convex-hull-in-python

        input:
            - ray:
                np array of shape (dim, )
            - convex_hull_points:
                np array of shape (dim, N)
        output:
            - intersection_point:
                np array of shape (dim, )
    '''
    eq = convex_hull.equations.T
    A, b = eq[:-1].T, eq[-1]
    ray /= np.linalg.norm(ray)
    alpha = np.divide(-b, (A @ ray.reshape(-1,1)).squeeze())
    intersection_point = np.ones_like(ray) * np.inf
    intersection_point_norm = np.inf
    for a in alpha:
        intersection_candidate = ray * a
        intersection_candidate_norm = np.linalg.norm(intersection_candidate)
        if (snap_close_values(A @ intersection_candidate.squeeze(),-b) <= -b).all() and intersection_candidate_norm < intersection_point_norm:
            intersection_point_norm = intersection_candidate_norm
            intersection_point = intersection_candidate
    return intersection_point
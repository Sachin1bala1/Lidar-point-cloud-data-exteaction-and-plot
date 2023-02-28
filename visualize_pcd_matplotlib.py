#!/usr/bin/env python3

import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

pointcloud = o3d.io.read_point_cloud("1876305444.pcd")

# o3d.visualization.draw_geometries([pointcloud])

pc_array = np.asarray(pointcloud.points)
print(pc_array)
# ax = plt.figure().add_subplot(projection='3d')
# ax.scatter(pc_array[:, 0], pc_array[:, 1], pc_array[:, 2], s=2)

# plt.show()
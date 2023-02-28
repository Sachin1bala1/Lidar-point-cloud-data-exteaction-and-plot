#!/usr/bin/env python3

import numpy as np
import open3d as o3d

pointcloud = o3d.io.read_point_cloud("1876305444.pcd")

o3d.visualization.draw_geometries([pointcloud])
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 09:15:29 2017

@author: jev
"""
from __future__ import division

import matplotlib.pyplot as plt
import numpy as np


# Det som trengs for plotting i 3D
def f_example1(x, y):
    return np.sin(y)+x**2*y


x = np.linspace(-1, 1, num=21)
y = np.linspace(-1, 1, num=21)
X, Y = np.meshgrid(x, y)
Z = f_example1(X, Y)

fig1 = plt.figure()
ax = fig1.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
plt.show()

fig2 = plt.figure()
ax = fig2.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z)
plt.show()


def f_example2(x, y):
    return np.sqrt(1-x**2-y**2)


x = np.linspace(-1, 1, num=201)
y = np.linspace(-1, 1, num=201)
X, Y = np.meshgrid(x, y)
Z = f_example2(X, Y)

fig1 = plt.figure()
ax = fig1.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z)
plt.show()

# Eksempel med setting av diverse ekstra parametre
fig = plt.figure()
x = np.linspace(-3, 5, num=81)
y = np.linspace(-10, 10, 201)
X, Y = np.meshgrid(x, y)
Z = f_example1(X, Y)
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(X, Y, Z)
ax.set_xlim3d(-4, 6)
ax.set_ylim3d(-12, 12)
ax.set_zlim3d(-50, 50)
ax.set_ylabel('Y er nord/sør')
ax.set_xlabel('X er øst/vest')
ax.set_zlabel('z er høyde over havet')
plt.title('Dette er tittelen på figuren')
plt.show()

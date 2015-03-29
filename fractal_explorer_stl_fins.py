#!/usr/bin/env python

import sys
import math
import geometry

#prisms = [[(0,0,0), (40,0,0), (5,20,0), (25,20,0),
#    (0,0,0.7), (40,0,0.7), (5,20,0.7), (25,20,0.7)]]

def add_one_layer(prisms, which=-1, scale=0.54):
  last_layer = prisms[which][:]
  dir = [0., last_layer[2][1] - last_layer[0][1],
         last_layer[2][2] - last_layer[0][2]]
  for count in xrange(2):
    new_layer = []
    sin_t = math.sin(math.pi/3)
    cos_t = math.cos(math.pi/3)
    if count == 1:
      sin_t = math.sin(-math.pi/3)
      cos_t = math.cos(-math.pi/3)
    for point_count, point in enumerate(last_layer):
      current = [(11.0+point[0])*scale,
                 (point[1]-last_layer[0][1])*scale,
                 (point[2]-last_layer[0][2])*scale]
      new_layer.append([current[0],
                        current[1]*cos_t - current[2]*sin_t + last_layer[2][1],
                        current[2]*cos_t + current[1]*sin_t + last_layer[2][2]])
#      new_layer.append([current[0],
#                        current[1]*cos_t - current[2]*sin_t + dir[1],
#                        current[2]*cos_t + current[1]*sin_t + dir[2]])
    prisms.append(new_layer)

def print_face(face1, face2, face3):
  print 'facet normal 0 0 0'
  print 'outer loop'
  print 'vertex', str(face1[0]), str(face1[1]), str(face1[2])
  print 'vertex', str(face2[0]), str(face2[1]), str(face2[2])
  print 'vertex', str(face3[0]), str(face3[1]), str(face3[2])
  print 'endloop'
  print 'endfacet'

def print_prisms(prisms):
  print 'solid fractal_explorer_stl_fins'
  for prism in prisms:
    print_face(prism[0], prism[1], prism[2])
    print_face(prism[1], prism[2], prism[3])
    print_face(prism[0], prism[4], prism[1])
    print_face(prism[1], prism[4], prism[5])
    print_face(prism[2], prism[4], prism[6])
    print_face(prism[7], prism[4], prism[6])
    print_face(prism[2], prism[3], prism[6])
    print_face(prism[7], prism[3], prism[6])
    print_face(prism[0], prism[2], prism[4])
    print_face(prism[6], prism[2], prism[4])
    print_face(prism[4], prism[5], prism[6])
    print_face(prism[5], prism[6], prism[7])
  print 'endsolid fractal_explorer_stl_fins'

def thickenate(prisms,
               thicknessMap={0:1.0, 1:0.9, 2:0.8, 3:0.7, 4:0.7, 5:0.7},
               minThickness=0.6):
  for count, prism in enumerate(prisms):
    thickness = minThickness
    if count > 0:
      layer_count = int(math.log(count, 2))
    else:
      layer_count = 0
    if layer_count in thicknessMap.keys():
      thickness = thicknessMap[layer_count]
    bMinusA = geometry.getNormalVector(prism[1], prism[0])
    cMinusA = geometry.getNormalVector(prism[2], prism[0])
    normal = geometry.normalizeVector(geometry.cross(bMinusA, cMinusA))
    for point in prism:
      for coord in xrange(3):
        point[coord] = point[coord] - normal[coord] * thickness/2.0
    newPoints = []
    for point in prism:
      newPoint = []
      for coord in xrange(3):
        newPoint.append(point[coord] + normal[coord] * thickness)
      newPoints.append(newPoint)
    prism.extend(newPoints)

prisms = [[[5.,0.,0.], [50.,0.,0.], [8.5,20.,0.], [33.,20.,0.]]]
for count in xrange(1000):
  add_one_layer(prisms, count)
thickenate(prisms)
print_prisms(prisms)

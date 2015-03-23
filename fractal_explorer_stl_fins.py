#!/usr/bin/env python

#prisms = [[(0,0,0), (40,0,0), (5,20,0), (25,20,0),
#    (0,0,0.7), (40,0,0.7), (5,20,0.7), (25,20,0.7)]]

def add_one_layer(prisms, scale, thickness=0.7):
  last_layer = prisms[-1]
  z = last_layer[1][0] - last_layer[0][0]
  y = thickness
  x = last_layer[2][1] - last_layer[0][1]
  delta_z = last_layer[2][0] - last_layer[0][0]
  delta_top_z = last_layer[1][0] - last_layer[3][0]
  

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

prisms = [[(0,0,0), (40,0,0), (5,20,0), (25,20,0),
    (0,0,0.7), (40,0,0.7), (5,20,0.7), (25,20,0.7)]]
add_one_layer(prisms)

print_prisms(prisms, 0.6)
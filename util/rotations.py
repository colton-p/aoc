"""
Direction vector rotations.
"""
import math

class DIR:
  """
  Direction vector constants
  """
  UP = (0, -1)
  DOWN = (0, 1)
  LEFT = (-1, 0)
  RIGHT = (1, 0)

  NORTH = UP
  SOUTH = DOWN
  WEST = LEFT
  EAST = RIGHT

def turn_right(dir):
  """
  Rotate direction vector right (clockwise).
  """
  return (-dir[1], dir[0])

def turn_left(dir):
  """
  Rotate direction vector left (counter-clockwise).
  """
  return (dir[1], -dir[0])

def turn_180(dir):
  """
  Rotate direction vector 180 degrees.
  """
  return (-dir[0], -dir[1])

def rotate_n_degrees(dir, deg):
  """
  Rotate deg degrees clockwise
  """
  rad = math.radians(deg)
  return rotate_n_rads(dir, rad)

def rotate_n_rads(dir, rad):
  """
  Rotate rad radians clockwise
  """
  (x, y) = dir

  return (
    x * math.cos(rad) - y * math.sin(rad),
    x * math.sin(rad) + y * math.cos(rad)
  )

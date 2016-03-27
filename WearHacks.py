from visual import *

light1 = sphere(pos = (-2,-2,-2), radius = 0.1, color = color.yellow)
light2 = sphere(pos = (-2,2,-2), radius = 0.1, color = color.yellow)
light3 = sphere(pos = (2,2,-2), radius = 0.1, color = color.yellow)
light4 = sphere(pos = (2,-2,-2), radius = 0.1, color = color.yellow)
light5 = sphere(pos = (-2,-2,2), radius = 0.1, color = color.yellow)
light6 = sphere(pos = (-2,2,2), radius = 0.1, color = color.yellow)
light7 = sphere(pos = (2,2,2), radius = 0.1, color = color.yellow)
light8 = sphere(pos = (2,-2,2), radius = 0.1, color = color.yellow)

wall1 = box(pos=(0,0,0), size=(0.2,6,6), color=color.white)
wall2 = box(pos=(0,0,0), size=(6,0.2,6), color=color.white)
floor = box(pos=(0,0,-2), size=(6,6,0.2), color=color.white)

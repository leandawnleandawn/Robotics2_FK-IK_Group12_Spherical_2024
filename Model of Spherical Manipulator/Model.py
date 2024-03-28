import math
from roboticstoolbox import SerialLink, PrismaticDH, RevoluteDH


def defineLinks():
    a1 = float(input("a_1 Link [mm]>>>"))
    a2 = float(input("a_2 Link [mm]>>>"))
    a3 = float(input("a_3 Link [mm]>>>"))
    return a1, a2, a3

a1, a2, a3 = defineLinks()

H01 = RevoluteDH(a1, 0, math.pi/2, 0, [-math.pi/2, math.pi/2])
H12 = RevoluteDH(0, 0, math.pi/2, math.pi/2, [-math.pi/2, math.pi/2])
H23 = PrismaticDH(0,0,0,a2+a3,[0, 0.05])


sphericalManipulator = SerialLink([H01, H12, H23])

print(sphericalManipulator)
sphericalManipulator.teach([0,0,0])

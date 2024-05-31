import roboticstoolbox as rtb
from spatialmath.base import *
from spatialmath import SE3


# Robot Static Kinematics
robotic_arm = rtb.models.URDF.Panda()
# print(robotic_arm)


# Calculating Forward Kinematics
fk_tran_m = robotic_arm.fkine([1.911, 0.8322, -0.4118, -1.557, -2.733, 0.8391, -0.5577])
# print(fk_tran_m)


# Calculating Inverse Kinematics
point = SE3(0.0, 0.7,0.5)
ik_tran_m = robotic_arm.ikine_LM(point)
print(ik_tran_m)
from src.robotics import kinematics as kin
print(kin.Rz(90))
print("----------------")
print(kin.Tz(9.9))
print("----------------")
print(kin.denavit(2, 12, 5, 45))
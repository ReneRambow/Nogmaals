from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
for i in range(9):
    robotArm.moveRight()

for i in range(9):

    robotArm.moveLeft()
    robotArm.grab()

    if robotArm.scan() == 'white':
        robotArm.moveRight()
        robotArm.drop()
        robotArm.moveLeft()
    else:
        robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
for s in range(9):

    robotArm.grab()
    if robotArm.scan() == 'red':

        for r in range(9-s):
            robotArm.moveRight()

        robotArm.drop()

        for l in range(8-s):
            robotArm.moveLeft()
    else:
        robotArm.drop()
        robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
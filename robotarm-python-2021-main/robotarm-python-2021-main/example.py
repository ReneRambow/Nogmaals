from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
for stapel in range(5):

    robotArm.grab()

    for i in range(9 - (stapel * 2)):
        robotArm.moveRight()

    robotArm.drop()

    for i in range(9 - (stapel * 2)):
        robotArm.moveLeft()

    robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
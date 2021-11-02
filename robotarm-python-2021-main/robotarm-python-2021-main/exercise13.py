from RobotArm import RobotArm

robotArm = RobotArm('exercise 13')
robotArm.randomLevel(1, 7)
# Jouw python instructies zet je vanaf hier:
i = 0
while robotArm.grab():
    i += 1

    for t in range(i):
        robotArm.moveRight()

    robotArm.drop()

    for t in range(i):
        robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
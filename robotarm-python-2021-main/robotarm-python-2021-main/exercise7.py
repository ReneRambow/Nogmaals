from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 5


for aantalStapels in range(5):
    for aantalBlokken in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()

    robotArm.moveRight()
    robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait(10)
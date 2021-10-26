import random


def start_ronde():
    randomGetal = random.randrange(1, 1001)

    for geraden in range(10):
        geradenGetal = int(input('\n\n\n\nWelk getal denkt u dat het is?\n'))

        if randomGetal == geradenGetal:
            print('U heeft het goed geraden!')
            return True

        print(f'\n\n\n\n{geradenGetal} is {"onder" if geradenGetal < randomGetal else "boven"} het random getal')

        verschil = abs(randomGetal - geradenGetal)

        print(
            f'en u bent {"heel erg dichtbij" if verschil < 20 else "dichtbij" if verschil < 50 else "niet echt in de buurt"}')

    return False


if __name__ == '__main__':
    for ronde in range(20):
        if not start_ronde():
            print('U bent geeindigd met een score van ', ronde)

        print(f'Uw score is {ronde + 1}')

        if input('Wilt u doorgaan? (J/N)\n').lower().startswith('n'):
            break
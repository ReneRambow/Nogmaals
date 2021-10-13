# name of student: Rene Rambow
# number of student: 99066788
# purpose of program: €1 en €2 euro toevoegen
# function of program: wisselgeld toegeven met munten
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
if paid < toPay:
    print(f"Je hebt niet genoeg betaald. U moet nog {toPay-paid} centen bijbetalen")
    exit()
else:
    print("Je krijgt wisselgeld")

change = paid - toPay #

nrcvalue200 = 0
nrcvalue100 = 0
nrcvalue50 = 0
nrcvalue20 = 0
nrcvalue10 = 0
nrcvalue5 = 0
nrcvalue2 = 0
nrcvalue1 = 0


coinValue = 200 #

if change > 0: #
  
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #

    if nrCoins > 0: #
        print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
        nrCoinsReturned = int(input(f'How many coins of {coinValue} cents did you return? ')) #


        change -= nrCoinsReturned * coinValue #
    
    if coinValue == 200:
      nrCoinsReturned200 = nrCoinsReturned
      coinValue = 100
    elif coinValue == 100:
      nrCoinsReturned100 = nrCoinsReturned
      coinValue = 50
    elif coinValue == 50:
      nrCoinsReturned50 = nrCoinsReturned
      coinValue = 20
    elif coinValue == 20:
      nrCoinsReturned20 = nrCoinsReturned
      coinValue = 10
    elif coinValue == 10:
      nrCoinsReturned10 = nrCoinsReturned
      coinValue = 5
    elif coinValue == 5:
      nrCoinsReturned5 = nrCoinsReturned
      coinValue = 2
    elif coinValue == 2:
      nrCoinsReturned2 = nrCoinsReturned
      coinValue = 1
    elif coinValue == 1:
      nrCoinsReturned1 = nrCoinsReturned
      coinValue = 0
    


# comment on code below: 
    

print("""----------------------------------""")
print(f'2 euro munten terug gegeven:    {nrCoinsReturned200}')
print(f'1 euro munten terug gegeven:    {nrCoinsReturned100}')
print(f'50 cent munten terug gegeven:   {nrCoinsReturned50}')
print(f'20 cent munten terug gegeven:   {nrCoinsReturned20}')
print(f'10 cent munten terug gegeven:   {nrCoinsReturned10}')
print(f'5 cent munten terug gegeven:    {nrCoinsReturned5}')
print(f'2 cent munten terug gegeven:    {nrCoinsReturned2}')
print(f'1 cent munten terug gegeven:    {nrCoinsReturned1}')
print("""----------------------------------""")
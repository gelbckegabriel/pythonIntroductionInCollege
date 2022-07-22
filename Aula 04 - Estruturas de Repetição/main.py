# make a program that writes the values between a and b (chosen by the user) and that is an even number.
a = int(input('Type one number: '))
b = int(input('Type another number that is bigger than the first: '))

while (a <= b):
   if (a % 2 == 0):
     print(a)
   a = a + 1

if (a > b):
  print('The first number is bigger than the second, try again!')

# make a program that will ask the user for a value and will only finish when he types a number that is positive and bigger than zero.
valor = int(input('Type a number that is positive and bigger than zero: '))
while (valor <= 0):
  valor = int(input('Type a number that is positive and bigger than zero: '))
print('The value is "{}". Shutting program down!' .format(valor))

# make a program that prints what the user type and stop it if the user types "leave".
print("Type anything you want ('Leave' to shut the program down)")
inputUser = input('Type: ')

while True:
    print(inputUser)
    inputUser = input('Type: ')
    if (inputUser == 'Leave'):
        break
print('Program has been shutted.')

# make a login with a continue and a break
while True:
    name = input('What´s your name? ')
    if (name != 'gelbcke'):
        continue
    password = input('What´s your password? ')
    if (password == 'User123'):
        break
print('Access granted!')

# FOR structure.
for i in range (6):
    print(i)

for i in range (10, 0, -2):
    print(i)

# Make a program that gets the average value between 1 and 100 (1 and 100 included) - using FOR.
amount = 0
plus = 0

for i in range (1, 101):
    if (i % 2 == 0):
        amount += i
        plus += i
average = plus / amount
print(i)
print(amount)
print(average)
# Add two values and make a simple conditional structure to tell which is bigger.
value1 = int(input('Type a number: '))
value2 = int(input('Type another number: '))

if (value1 > value2):
    print('The first number is bigger than the second.')

print('------------------------------------------------')

# Add a value and make a composite conditional structure to tell if it´s even or odd.
number = int(input('Type any number: '))

if (number % 2 == 0):
    print('This is an even number.')
else:
    print('This is an odd number')

print('------------------------------------------------')

# Create a student that take 3 different classes and needs to have an average grade of 7 to pass using logic expressions.
mathCourse = 7.5;
historyCourse = 7;
portugueseCourse = 5.5;

if (mathCourse >= 7 and historyCourse >= 7 and portugueseCourse >= 7):
    print('You´ve passed')
else:
    print('You haven´t passed. Try again next year!')

print('------------------------------------------------')

# Let the user choose if he wants to buy apples, oranges or bananas. It should be shown a menu at the start with the option 1, 2 or 3, than choose the amount and give the user the full value of the purchase.
print(" Uncle Zé´s Fruit Shop ")
print('-----------------------')
print('    Choose a fruit:    ')
print('ID: 1 - Apples - U$1.99')
print('ID: 2 - Oranges - U$4.57')
print('ID: 3 - Bananas - U$3.67')
print('-----------------------')
answer = int(input('Type the "ID" to choose: '))
amount = int(input('Type the amount you want: '))
print('-----------------------')

if (answer == 1):
    total = 1.99 * amount
    print('You´ve bought {} APPLES. The total is U$ %.2f '.format(amount) % total)
else:
    if (answer == 2):
        total = 4.57 * amount
        print('You´ve bought {} ORANGES. The total is U$ %.2f '.format(amount) % total)
    else:
        if (answer == 3):
            total = 3.67 * amount
            print('You´ve bought {} BANANAS. The total is U$ %.2f '.format(amount) %total)
        else:
            print('This product doesn´t exist!')

print('------------------------------------------------')

# Add two values and make a simple conditional structure to tell which is bigger.
value1 = int(input('Type a number: '))
value2 = int(input('Type another number: '))

if (value1 > value2):
    print('The first number is bigger than the second.')

print('------------------------------------------------')

# Add a value and make a composite conditional structure to tell if it´s even or odd.
number = int(input('Type any number: '))

if (number % 2 == 0):
    print('This is an even number.')
else:
    print('This is an odd number')

print('------------------------------------------------')

# Create a student that take 3 different classes and needs to have an average grade of 7 to pass using logic expressions.
mathCourse = 7.5;
historyCourse = 7;
portugueseCourse = 5.5;

if (mathCourse >= 7 and historyCourse >= 7 and portugueseCourse >= 7):
    print('You´ve passed')
else:
    print('You haven´t passed. Try again next year!')

print('------------------------------------------------')

# Let the user choose if he wants to buy apples, oranges or bananas. It should be shown a menu at the start with the option 1, 2 or 3, than choose the amount and give the user the full value of the purchase.
print(" Uncle Zé´s Fruit Shop ")
print('-----------------------')
print('    Choose a fruit:    ')
print('ID: 1 - Apples - U$1.99')
print('ID: 2 - Oranges - U$4.57')
print('ID: 3 - Bananas - U$3.67')
print('-----------------------')
answer = int(input('Type the "ID" to choose: '))
amount = int(input('Type the amount you want: '))
print('-----------------------')

if (answer == 1):
    total = 1.99 * amount
    print('You´ve bought {} APPLES. The total is U$ %.2f '.format(amount) % total)
else:
    if (answer == 2):
        total = 4.57 * amount
        print('You´ve bought {} ORANGES. The total is U$ %.2f '.format(amount) % total)
    else:
        if (answer == 3):
            total = 3.67 * amount
            print('You´ve bought {} BANANAS. The total is U$ %.2f '.format(amount) %total)
        else:
            print('This product doesn´t exist!')

print('------------------------------------------------')

# Repeat the last exercise using the multiple choice structure usign ELIF.
print("     Uncle Zé´s Fruit Shop ")
print('--------------------------------')
print('        Choose a fruit:    ')
print('    ID: 1 - Apples - U$1.99')
print('    ID: 2 - Oranges - U$4.57')
print('    ID: 3 - Bananas - U$3.67')
print('----------------------------------')
answer = int(input('    Type the "ID" to choose: '))
amount = int(input('    Type the amount you want: '))
print('----------------------------------')

if (answer == 1):
    total = 1.99 * amount
    print('You´ve bought {} APPLES. The total is U$ %.2f '.format(amount) % total)
elif (answer == 2):
    total = 4.57 * amount
    print('You´ve bought {} ORANGES. The total is U$ %.2f '.format(amount) % total)
elif (answer == 3):
    total = 3.67 * amount
    print('You´ve bought {} BANANAS. The total is U$ %.2f '.format(amount) %total)
else:
    print('This product doesn´t exist!')

print('------------------------------------------------')

# Verify a person´s name, if it´s equal to 'Gabriel', put it on the screen, if it isn´t ask his/her age and if it´s younger than 18 say it´s a minor if it´s older than 100 say that this person probably doesn´t exist.
name = input('Type your name: ')

if (name == 'Gabriel'):
    print('Welcome back Sir!')
else:
    age = int(input('Type your age: '))
    if (age < 18):
        print('You´re under age.')
    elif (age > 100):
        print('This person probably doesn´t exist!')
# TUPLES - Those are static.
bagTuple = ('Axe', 'T-Shirt', 'Bacon', 'Avocado');
print(bagTuple);
print(bagTuple[1]);
print(bagTuple[0:2]);
print(bagTuple[2:]);

for item in bagTuple:
    print('I have in my bag: {}' .format(item))

print('-' * 40);

# LISTS - Same thing as an array.
bagList = ['Axe', 'T-Shirt', 'Bacon', 'Avocado'];
bagList[3] = 'Orange';
print(bagList)

bagList.append('Avocado');
bagList.insert(2, 'Jacket');
del bagList[4]; # or you can use bagList.remove('Orange');
print(bagList)

print('-' * 40);

# DOUBLE INDEXATION WITH STRINGS - IT CAN BE TRIPLE AND ESCALATING.
doubleIndexation = ['This', 'is', 'an', 'example'];
print('We are accessing the letter x (index 1) from the 4° word (index 3) = ' + '"' + doubleIndexation[3][1] + '"')

print('-' * 40);

# LIST INSIDE OF A LIST.
listInsideOfList = [['Onion', 0.39], ['Tomato', 0.78], ['Banana', 1.47]];
print(listInsideOfList);
print(listInsideOfList[0][1]);

print('-' * 40);

# Develop a program that will receive name, amount and value of a groceries item and add to a list.
item = [];
market = [];

for i in range(3):
    item.append(input('Type the name of the item: '));
    item.append(int(input('Type the amount of the item: ')));
    item.append(float(input('Type the price of the item: ')));
    market.append(item[:]);
    item.clear();
    print(market);

plus = 0;
print('Shopping list: ')
print('-' * 20)
print('item | amount | price | total')
for item in market:
    print('{} | {} | {} | {}' . format(item[0], item[1], item[2], item[1] * item[2]))
    plus = plus + item[1] * item[2]
print('-' * 20)
print('Total value: U$%.2f' % plus)

print('-' * 40);

# DICTIONARY - SEEMS LIKE AN OBJECT.
game = {
    'name': 'The Last of Us',
    'publisher': 'Naughty Dog',
    'year': 2013
}
print(game);
print(game['name'])
print('---')
print(game.values())
print(game.keys())
print(game.items())
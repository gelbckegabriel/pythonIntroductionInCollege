def subtraction(value1, value2):
    print(value1 - value2);

subtraction(5, 7);

# Write a function that creates a border around the word that should be received as a parameter. Emphasizing the word.
def title(text):
    print('+', '-' * len(text), '+');
    print('|', text, '|');
    print('+', '-' * len(text), '+');

title('Gelbcke');

# Global instruction.
def food():
    global eggs;
    eggs = 'food';

eggs = 'breakfast';
food();
print(eggs);

# Write a function to verify a string, it receives the string, the minimum and maximum number of characters. return true if the size of the string is between the min and max, and false otherwise.
def checker(string, minimum, maximum):

    if( len(string) < minimum or len(string) > maximum ):
        return 'false';
    else:
        return 'true';

result = checker('Gelbcke', 2, 7);
print('The information typed is "{}" ! \nShutting program down...' .format(result));

# TRY and EXCEPT.
while True:
    try:
        a = int(input('Type a number: '));
        break
    except ValueError:
        print('Characters incorret. Try again!')

# LAMBDA.
res = lambda x: x * x;
print(res(3))
plus = lambda number1, number2: number1 + number2;
print(plus(5, 5))
import random

data = ''


def requesting_data():
    global data

    print('Print a random string containing 0 or 1:')
    user_input = input()

    for chara in user_input:
        if chara not in ('0', '1'):
            user_input.strip(chara)
        else:
            data += chara


requesting_data()
while len(data) < 100:
    print(f'Current data length is {len(data)}, {100 - len(data)} symbols left')
    requesting_data()
else:
    print(f'Final data string:\n{data}')

triads = ['000', '001', '010', '011', '100', '101', '110', '111']
counting_dict = {}
for triad in triads:
    temp_data = data
    i = 0
    j = 0
    while len(temp_data) > 3:
        if temp_data.startswith(triad):
            if temp_data[3] == '0':
                i += 1
            elif temp_data[3] == '1':
                j += 1
        temp_data = temp_data[1:]
    else:
        counting_dict[triad] = [i, j]

print('''You have $1000. Every time the system successfully predicts your next press, you lose $1.
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!''')

balance = 1000


def game():
    global counting_dict
    global balance
    global user_string

    test_string = ''

    for char in user_string:
        if char in ('0', '1'):
            test_string += char

    prediction = str(random.randint(0, 1)) * 3

    for p in range(len(test_string) - 3):
        test_triad = test_string[p:p+3]
        if counting_dict[test_triad][0] == counting_dict[test_triad][1]:
            prediction += str(random.randint(0, 1))
        elif counting_dict[test_triad][0] > counting_dict[test_triad][1]:
            prediction += '0'
        elif counting_dict[test_triad][0] < counting_dict[test_triad][1]:
            prediction += '1'

    print(f'prediction:\n{prediction}')

    test_list = list(test_string)
    prediction_list = list(prediction)
    k = 0
    for n in range(3, len(test_list)):
        if test_list[n] == prediction_list[n]:
            k += 1

    print(f'Computer guessed right {k} out of {len(test_list) - 3} symbols ({round(k / (len(test_list) - 3) *100, 2)}%)')
    balance -= k
    balance += len(test_list) - 3 - k
    print(f'Your capital is now ${balance}')


while True:
    print('Print a random string containing 0 or 1:')
    user_string = input()
    if user_string == "enough":
        print("Game over!")
        break
    elif user_string.isalnum():
        game()

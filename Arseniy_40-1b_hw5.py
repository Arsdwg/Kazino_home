import logic
from decouple import config


total = int(config('MY_MONEY'))
while total > 0:
    print('У вас ' + str(total) + '$')
    enter = int(input('Введите вашу ставку - '))
    if enter > total:
        print("У вас нет столько денег!")
        continue

    number = int(input('Введите цифру на которую поставите (от 1 до 10)- '))
    if number > logic.win[-1]:
        print("Такого числа нет!")
        continue

    total -= enter
    chance = logic.won
    if number == chance:
        print(f'Число было {chance}')
        total += enter * 2
        print(f'Вы выиграли {enter * 2}$')
        print(f'У вас {total}$')
    else:
        print(f'Число было {chance}')
        print(f'Вы проиграли {enter}$')
        print(f'У вас {total}$')
    farther = input('Вы хотите продолжить игрy?(y/n) ')

    if total == 0:
        print('Вы разорились(')
        break

    if farther == 'n':
        if total < int(config('MY_MONEY')):
            raz = int(config('MY_MONEY')) - total
            print(f'Вы в минусе на {raz}\n Казино это плохо(')
            print('///exiting///')
            break
        else:
            raz = total - int(config('MY_MONEY'))
            print(f'Вы в плюсе на {raz}\nКазино значит круто)')
            print('///exiting///')
            break
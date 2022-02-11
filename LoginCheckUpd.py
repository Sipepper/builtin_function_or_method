import sys

base = {'Sipep': 'qwerty321', 'Nagibator24': 'uzumymw432', 'Dmitry': 'JcnsHsywhNhdu212'}


def authenticate() -> bool:
    return True


def check_password(username: 'str', password: 'str') -> bool:
    return base.get(username) == password


def auth(func):
    def wrapper(username, password):
        if not check_password(username, password):
            return False
        if not authenticate():
            return False
        return func(username, password)

    return wrapper


@auth
def login(username, password):
    return True


try:
    cmd_user = sys.argv[1]
    cmd_pass = sys.argv[2]
except IndexError:
    cmd_user = None
    cmd_pass = None

if __name__ == '__main__':
    for i in range(4):
        if cmd_user in base.keys and cmd_pass is None:
            if login(cmd_user, input('Введите пароль: ')):
                print('Вы в системе!')
                break
            else:
                print(f'Неверный пароль у вас осталось {3 - i} попытки')
        elif login(cmd_user,cmd_pass):
            print('Вы в системе')
            break
        elif i != 3:
            print(f'Неверное имя пользователя или пароль \nУ вас осталось {3 - i} попытки')
        else:
            print('У вас не осталось попыток')

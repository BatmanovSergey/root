
def check_name():
    l_n = input('Введите фамилию и инициалы нового сотрудника: ')
    if l_n != ' ' or not l_n.isdigit():
        return l_n 
    else:
        print('Введены не корректные данные!')
        check_name() 

def check_bus():
    b = input('Введите госномер автобуса: ')
    if b == '':
        return "None"
    else:
        return b
            
def check_route():
    r = input('Введите номер маршрута: ')
    if r.isdigit():
        return r
    elif r == '':
        return "None"
    else:
        print('Введены не корректные данные!')
        check_route()

def check_id():
    id_n = input('Введите id_сотрудника для удаления из базы данных: ')
    if id_n.isdigit():
        return int(id_n)
    else:
        print('Введены не корректные данные!')
        check_id()


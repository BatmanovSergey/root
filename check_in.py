import model as m

def check_type_num(data):
    if data.isdigit():
        return int(data)
    return -1

# проверка существования id
def check_id_exist(file, m_id):
    list_all_person = m.read_file(file)
    return m_id != -1 and m_id in range(len(list_all_person))

def check_id():
    id_n = input('Введите id_сотрудника для удаления из базы данных: ')
    if id_n.isdigit():
        return int(id_n)
    else:
        print('Введены не корректные данные!')
        check_id()


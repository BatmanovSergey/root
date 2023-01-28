import model as m
from os import path

def check_type_num(data):#prinimaem str, otdaem int
    if data.isdigit():
        return int(data)
    return -1

# # проверка существования id
def check_id_exist(file, m_id):#prinimaem int
    list_all_person = m.read_file(file)
    # print(list_all_person)
    temp = str(m_id)
    count = 0
    for i in range(1,len(list_all_person)):
        # print(list_all_person[i][0])
        if list_all_person[i][0] == temp:
            count += 1
    if count > 0:
        return m_id
    else:
        return -1
   

# def check_id():
#     id_n = input('Введите id_сотрудника для удаления из базы данных: ')
#     if id_n.isdigit():
#         return int(id_n)
#     else:
#         print('Введены не корректные данные!')
#         check_id()


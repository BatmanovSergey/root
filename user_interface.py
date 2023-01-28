from logger import logging
import model as m
import check_in
from prettytable import PrettyTable

def menu():
    print()
    print('Информационая система корабля "ПЕРШЕРОН" привествует Вас!')
    logging.info('Start program')
    while True:
        type_num = input('\n*****Главное меню*****\nВыберите пункт меню:\n'
                         '1 - Показать все записи\n'
                         '2 - Найти запись\n'
                         '3 - Добавить запись\n'
                         '4 - Редактировать запись\n'
                         '5 - Удалить запись\n'
                         '0 - Выход\n')
        type_num = check_in.check_type_num(type_num)

        if type_num not in range(6):
            logging.error('Error: wrong main menu selection')
            print("Error. Try again")
            continue

        elif type_num == 1:  # показать все записи
            print('Информация по всем членам команды корабля "ПЕРШЕРОН"')
            m.get_table('Team.csv')
            print('Вы будете перемещены в главное меню.')

        elif type_num == 2:  # найти запись
            d = (input('Введите данные для поиска: '))
            m.find_info('Team.csv', d)
            print('Вы будете перемещены в главное меню.')

        elif type_num == 3:  # добавить запись
            print('Добавление новой записи...')
            m.add_text('Team.csv')
            print('Вы будете перемещены в главное меню.')

        elif type_num == 4:  # редактировать запись
            man_id = input('Введите id сотрудника, данные которого вы хотите изменить:\n') #stroka
            man_id = check_in.check_type_num(man_id)#int
            if man_id == -1:
                logging.error('Error: incorrect id entered.')
                print('id does not exist. Check right id one more time.')
            else:  
                r_man_id = check_in.check_id_exist('Team.csv', man_id)#peredaem int,prinimaem int
                if r_man_id == -1:
                    logging.error('Error: incorrect id entered.')
                    print('id does not exist. Check right id.')
                else:
                    num = input('\nКакие изменения вы хотите внести:\n' #stroka
                                '1 - Изменить фамилию\n'
                                '2 - Изменить имя\n'
                                '3 - Изменить должность\n'
                                '4 - Изменить год рождения\n'
                                '5 - Изменить все данные\n')
                    num = check_in.check_type_num(num) #int
                    if num in range(1, 6):
                        m.change_info('Team.csv', man_id, num)
                        print('Вы будете перемещены в главное меню.')
                    else:
                        logging.error('Error: wrong submenu selection')
                        print("Error. Try again")
                        continue
            

        elif type_num == 5:  # удалить запись
            man_id = input('Введите id сотрудника, данные которого вы хотите удалить:\n')
            man_id = check_in.check_type_num(man_id)#int
           
            if man_id == -1:
                logging.error('Error: incorrect id entered.')
                print('id does not exist. Enter right id.')
                # print('Вы будете перемещены в главное меню.')
            else:   
                r_man_id = check_in.check_id_exist('Team.csv', man_id)#peredaem int,prinimaem int
                # print(r_man_id)
                if r_man_id == -1:
                    logging.error('Error: incorrect id entered.')
                    print('id does not exist. Check right id.')
                    # print('Вы будете перемещены в главное меню.')
                
                else:
                    m.delete_info('Team.csv', r_man_id)
            print('Вы будете перемещены в главное меню.')

        elif type_num == 0:  # выход
            logging.info("Stop program")
            print('Спасибо, что воспользовались нашей информационной системой\n'
            'корабля. Желаем Вам всего наилучшего.\n'
            'До встречи на просторах бескрайней Галактики!!!')
            break


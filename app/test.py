# from models_kladr import Kladr
# from app import db
# from threading import Thread

# p = Kladr.query.filter(Kladr.code.contains('4600000000000')).all()
#
# def query_kladr():
#     for i in range(1, 100):
#         st = '0'
#         if i < 10:
#             st = '0' + str(i) + '00000000000'
#         else:
#             st = str(i) + '00000000000'
#         Kladr.query.filter(Kladr.tags.like('%00000000000')).all()
#         if not p == []:
#             p1 = p[0]
#             p2 = str(p1).split(':')
#             print('{} {} - {}'.format(p2[1], p2[3], str(i)))
#         # print(p2)
#
# def query_kladr2():
#     # '46 РРР ГГГ ППП АА'
#     global kladr_list
#     kladr_list = []
#     for i in range(1, 1000):
#         st = '0'
#         if i < 10:
#             st = '46' + '00' + str(i) + '00000000'
#         elif i >= 10 and i < 100:
#             st = '46' + '0' + str(i) + '00000000'
#         elif i >= 100:
#             st = '46' + str(i) + '00000000'
#         p = Kladr.query.filter(Kladr.code.contains(st)).all()
#
#         if not p == []:
#             p1 = p[0]
#             p2 = str(p1).split(':')
#             p3 = '{} {} - {}'.format(p2[1], p2[3], str(i))
#             kladr_list.append(p3)
#     return kladr_list
#
# p1 = Thread(target=query_kladr2)
# # p2 = Thread(target=wait_thread)
#
# def wait_thread():
#     chek = True
#     p1.start()
#     while chek:
#         chek = p1.isAlive()
#         print('Wait...')
#     print(kladr_list)


import dbf
import models_kladr
from app import db
from models_kladr import Kladr, Street, Doma, Altnames, Namemap, Socrbase, Flat

# db.create_all()
#
# def create_Kladr():
#     tables = dbf.Table('KLADR.dbf', codepage='cp866')
#     tables.open()
#     len_table = len(tables)  # Колличество записей
#     action = 0  # Счетчик действий
#     step = 50000  # Шаги
#     step_1 = len_table // step  # колличество шагов кратных step
#     step_2 = len_table % step  # колличество шагов меньше step
#     for i in tables:
#         p = Kladr(name=i['name'].replace(' ', ''),
#                   socr=i['socr'].replace(' ', ''),
#                   code=i['code'].replace(' ', ''),
#                   index=i['index'].replace(' ', ''),
#                   gninmb=i['gninmb'].replace(' ', ''),
#                   uno=i['uno'].replace(' ', ''),
#                   ocatd=i['ocatd'].replace(' ', ''),
#                   status=i['status'].replace(' ', ''))
#         db.session.add(p)
#         action = action + 1
#         if len_table > step:  # если колличество записей больше колличества шагов step
#             if action == step:  # если колличество действий сравнялось колличеству шагов step
#                 print(action)
#                 db.session.commit()  # вносим изменения вбазу
#                 print('session commit')
#                 step_1 = step_1 - 1  # уменьшаем колличество шагов кратных step
#                 print(step_1)
#                 action = 0
#             if step_1 == 0:
#                 if action == step_2:
#                     print(action)
#                     db.session.commit()
#                     action = 0
#                     print(len_table)
#         if len_table < step:
#             if action == len_table:
#                 print(action)
#                 db.session.commit()
#                 action = 0
#                 print(len_table)
#
#
# def create_street():
#     tables = dbf.Table('STREET.dbf', codepage='cp866')
#     tables.open()
#     len_table = len(tables)  # Колличество записей
#     action = 0  # Счетчик действий
#     step = 50000  # Шаги
#     step_1 = len_table // step  # колличество шагов кратных step
#     step_2 = len_table % step  # колличество шагов меньше step
#     for i in tables:
#         p = Street(name=i['name'].replace(' ', ''),
#                   socr=i['socr'].replace(' ', ''),
#                   code=i['code'].replace(' ', ''),
#                   index=i['index'].replace(' ', ''),
#                   gninmb=i['gninmb'].replace(' ', ''),
#                   uno=i['uno'].replace(' ', ''),
#                   ocatd=i['ocatd'].replace(' ', ''))
#         db.session.add(p)
#         action = action + 1
#         if len_table > step:  # если колличество записей больше колличества шагов step
#             if action == step:  # если колличество действий сравнялось колличеству шагов step
#                 print(action)
#                 db.session.commit()  # вносим изменения вбазу
#                 print('session commit')
#                 step_1 = step_1 - 1  # уменьшаем колличество шагов кратных step
#                 print(step_1)
#                 action = 0
#             if step_1 == 0:
#                 if action == step_2:
#                     print(action)
#                     db.session.commit()
#                     action = 0
#                     print(len_table)
#         if len_table < step:
#             if action == len_table:
#                 print(action)
#                 db.session.commit()
#                 action = 0
#                 print(len_table)
#
# def create_doma():
#     tables = dbf.Table('DOMA.dbf', codepage='cp866')
#     tables.open()
#     len_table = len(tables)  # Колличество записей
#     action = 0  # Счетчик действий
#     step = 50000  # Шаги
#     step_1 = len_table // step  # колличество шагов кратных step
#     step_2 = len_table % step  # колличество шагов меньше step
#     for i in tables:
#         p = Doma(name=i['name'].replace(' ', ''),
#                    korp=i['korp'].replace(' ', ''),
#                   socr=i['socr'].replace(' ', ''),
#                   code=i['code'].replace(' ', ''),
#                   index=i['index'].replace(' ', ''),
#                   gninmb=i['gninmb'].replace(' ', ''),
#                   uno=i['uno'].replace(' ', ''),
#                   ocatd=i['ocatd'].replace(' ', ''))
#         db.session.add(p)
#         action = action + 1
#         if len_table > step:  # если колличество записей больше колличества шагов step
#             if action == step:  # если колличество действий сравнялось колличеству шагов step
#                 print(action)
#                 db.session.commit()  # вносим изменения вбазу
#                 print('session commit')
#                 step_1 = step_1 - 1  # уменьшаем колличество шагов кратных step
#                 print(step_1)
#                 action = 0
#             if step_1 == 0:
#                 if action == step_2:
#                     print(action)
#                     db.session.commit()
#                     action = 0
#                     print(len_table)
#         if len_table < step:
#             if action == len_table:
#                 print(action)
#                 db.session.commit()
#                 action = 0
#                 print(len_table)
#
#
# create_doma()

code = '4600700100500'


def altnames_kladr(code):
    if code[-2:] == '51':
        code = code[:-2] + '00'
        address = Altnames.query.filter(Altnames.oldcode.like(code)).first()
        code = address.newcode
        return code
    else:
        return code

print(altnames_kladr(code))
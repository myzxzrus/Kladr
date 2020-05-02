from models_kladr import Kladr
from app import db
from threading import Thread

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



p = Kladr.query.filter(Kladr.code.like('%00000000000')).all()

for i in p:
    str = '{} {}'.format(i.name, i.socr)
    print(str)











|
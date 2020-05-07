from flask import Blueprint
from flask import render_template
from models_kladr import Kladr, Street


kladr = Blueprint('kladr', __name__, template_folder='templates')

# def query_kladr():
#     kladr_list = []
#     for i in range(1, 100):
#         st = '0'
#
#         if i < 10:
#             st = '0' + str(i) + '00000000000'
#         else:
#             st = str(i) + '00000000000'
#         p = Kladr.query.filter(Kladr.code.contains(st)).all()
#         if not p == []:
#             p1 = p[0]
#             p2 = str(p1).split(':')
#             p3 = '{} {} - {}'.format(p2[1], p2[3], str(i))
#         kladr_list.append(p3)
#     return kladr_list


@kladr.route('/')
def index():
    kladrs = Kladr.query.filter(Kladr.code.like('%00000000000')).all()
    return render_template('kladr/index.html', kladrs=kladrs)

'''Передаем уровень вхождения в kladr # 'CC РРР ГГГ ППП АА' '''

@kladr.route('/<region>')  # <region> имя параметра
def kladr_region(region):
    # for region
    like_district = '{}___000000__'.format(region)
    like_citi = '{}000___000__'.format(region)
    like_settlement = '{}000000_____'.format(region)
    # 46 000 001 000 00 - Citi 4600000100000 1600 - street
    like_street = '{}000000000______'.format(region)
    notquery = '{}00000000000'.format(region)
    address = Kladr.query.filter(Kladr.code.like(notquery)).all()
    district = Kladr.query.filter(Kladr.code.like(like_district), Kladr.code != notquery).all()
    citi = Kladr.query.filter(Kladr.code.like(like_citi), Kladr.code != notquery).all()
    settlement = Kladr.query.filter(Kladr.code.like(like_settlement), Kladr.code != notquery).all()
    street = Street.query.filter(Street.code.like(like_street)).all()
    template_context = dict(district=district, citi=citi, settlement=settlement, street=street, address=address, code=notquery)
    return render_template('kladr/kladr_region.html', **template_context)


@kladr.route('/<region>/<subtotal_region>')  # <level> имя параметра
def kladr_subtotal_region(region, subtotal_region):
    # for distrikt
    if len(subtotal_region) == 3:
        like_citi = '{}___000__'.format(region+subtotal_region)
        like_settlement = '{}000_____'.format(region+subtotal_region)
        notquery = '{}00000000'.format(region+subtotal_region)
        citi = Kladr.query.filter(Kladr.code.like(like_citi), Kladr.code != notquery).all()
        settlement = Kladr.query.filter(Kladr.code.like(like_settlement), Kladr.code != notquery).all()
        address = Kladr.query.filter(Kladr.code.like(notquery)).all()
        template_context = dict(chek='districkt', citi=citi, settlement=settlement, address=address, code=notquery)
    # for citi
    if len(subtotal_region) == 11:
        like_settlement = '{}_____'.format(region + subtotal_region[:6])
        # 46 000 001 000 00 - Citi 4600000100000 1600 - street
        like_street = '{}______'.format(region + subtotal_region[:9])
        notquery = '{}'.format(region + subtotal_region)
        settlement = Kladr.query.filter(Kladr.code.like(like_settlement), Kladr.code != notquery).all()
        street = Street.query.filter(Street.code.like(like_street)).all()
        address = Kladr.query.filter(Kladr.code.like(notquery)).all()
        template_context = dict(chek='citi', street=street, settlement=settlement, address=address, code=notquery)
    # for settlement
    if len(subtotal_region) == 13:
        # 46 000 001 000 00 - Citi 4600000100000 1600 - street
        like_street = '{}______'.format(subtotal_region[:11])
        street = Street.query.filter(Street.code.like(like_street)).all()
        address = Kladr.query.filter(Kladr.code.like(subtotal_region)).all()
        template_context = dict(chek='settlement', street=street, address=address, code=subtotal_region)
    return render_template('kladr/kladr_subtotal_region.html', **template_context)


@kladr.route('/<region>/<subtotal_region>/<street>')  # <level> имя параметра
def kladr_street(region, subtotal_region, street):
    print(region, subtotal_region, street)
    # return render_template('kladr/kladr_subtotal_region.html', **template_context)
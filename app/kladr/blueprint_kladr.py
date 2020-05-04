from flask import Blueprint
from flask import render_template
from models_kladr import Kladr


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
    like_district = f'{region}___000000__'
    like_citi = f'{region}000___000__'
    like_settlement = f'{region}000000_____'
    district = Kladr.query.filter(Kladr.code.like(like_district)).all()
    citi = Kladr.query.filter(Kladr.code.like(like_citi)).all()
    settlement = Kladr.query.filter(Kladr.code.like(like_settlement)).all()
    template_context = dict(district=district, citi=citi, settlement=settlement)
    return render_template('kladr/kladr_region.html', **template_context)


@kladr.route('/<region>/<level_district>')  # <level> имя параметра
def kladr_district(region, level_district):
    # for distrikt
    like_citi = f'{region+level_district}___000__'
    like_settlement = f'{region+level_district}000_____'
    citi = Kladr.query.filter(Kladr.code.like(like_citi)).all()
    settlement = Kladr.query.filter(Kladr.code.like(like_settlement)).all()
    template_context = dict(citi=citi, settlement=settlement)
    return render_template('kladr/kladr_district.html', **template_context)
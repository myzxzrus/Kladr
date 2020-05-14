from flask import Blueprint
from flask import render_template
from models_kladr import Kladr, Street, Doma, Altnames


kladr = Blueprint('kladr', __name__, template_folder='templates')

def altnames_kladr(code):
    if code[-2:] == '51':
        code = code[:-2] + '00'
        address = Altnames.query.filter(Altnames.oldcode.like(code)).first()
        return address.newcode
    else:
        return code



@kladr.route('/')
def index():
    kladrs = Kladr.query.filter(Kladr.code.like('%00000000000')).all()
    return render_template('kladr/index.html', kladrs=kladrs)

'''Передаем уровень вхождения в kladr # 'CC РРР ГГГ ППП АА' '''

@kladr.route('/<region>')  # <region> имя параметра
def kladr_region(region):
    print('kladr_region')
    # for region
    like_district = '{}___000000__'.format(region)
    like_citi = '{}000___000__'.format(region)
    like_settlement = '{}000000_____'.format(region)
    # 46 000 001 000 00 - Citi 4600000100000 1600 - street СС РРР ГГГ ППП УУУУ АА
    like_street = '{}000000000______'.format(region)
    notquery = '{}00000000000'.format(region)
    address = Kladr.query.filter(Kladr.code.like(notquery)).all()
    district = Kladr.query.filter(Kladr.code.like(like_district), Kladr.code != notquery).order_by(Kladr.name).all()
    citi = Kladr.query.filter(Kladr.code.like(like_citi), Kladr.code != notquery).order_by(Kladr.name).all()
    settlement = Kladr.query.filter(Kladr.code.like(like_settlement), Kladr.code != notquery).order_by(Kladr.name).all()
    street = Street.query.filter(Street.code.like(like_street)).order_by(Street.name).all()
    template_context = dict(district=district, citi=citi, settlement=settlement, street=street, address=address, code=notquery)
    return render_template('kladr/kladr_region.html', **template_context)


@kladr.route('/<region>/<subtotal_region>')  # <level> имя параметра
def kladr_subtotal_region(region, subtotal_region):
    # for distrikt
    print('kladr_subtotal_region')
    if len(subtotal_region) == 3:
        like_citi = '{}___000__'.format(region+subtotal_region)
        like_settlement = '{}000_____'.format(region+subtotal_region)
        notquery = '{}00000000'.format(region+subtotal_region)
        citi = Kladr.query.filter(Kladr.code.like(like_citi), Kladr.code != notquery).order_by(Kladr.name).all()
        settlement = Kladr.query.filter(Kladr.code.like(like_settlement), Kladr.code != notquery).order_by(Kladr.name).all()

        address = Kladr.query.filter(Kladr.code.like(notquery)).all()
        template_context = dict(chek='districkt', citi=citi, settlement=settlement, address=address, code=notquery)
    # for citi
    if len(subtotal_region) == 11:
        like_settlement = '{}_____'.format(region + subtotal_region[:6])
        # 46 000 001 000 00 - Citi 4600000100000 1600 - street
        like_street = '{}______'.format(region + subtotal_region[:9])
        notquery = '{}'.format(region + subtotal_region)
        settlement = Kladr.query.filter(Kladr.code.like(like_settlement), Kladr.code != notquery).order_by(Kladr.name).all()
        street = Street.query.filter(Street.code.like(like_street)).order_by(Street.name).all()
        altnames = altnames_kladr(notquery)
        print(altnames)
        address = Kladr.query.filter(Kladr.code.like(notquery)).all()
        print(address)
        template_context = dict(chek='citi', street=street, settlement=settlement, address=address, code=notquery, altnames=altnames)
    # for settlement
    if len(subtotal_region) == 13:
        # 46 000 001 000 00 - Citi 4600000100000 1600 - street
        like_street = '{}______'.format(subtotal_region[:11])
        street = Street.query.filter(Street.code.like(like_street)).order_by(Street.name).all()
        altnames = altnames_kladr(subtotal_region)
        address = Kladr.query.filter(Kladr.code.like(subtotal_region)).all()
        print(altnames)
        print(address)
        template_context = dict(chek='settlement', street=street, address=address, code=subtotal_region, altnames=altnames)
    return render_template('kladr/kladr_subtotal_region.html', **template_context)


@kladr.route('/<region>/<subtotal_region>/<street>')  # <level> имя параметра
def kladr_street(region, subtotal_region, street):
    print('kladr_street')
    # if len(subtotal_region) == 13:
    # 46 00000100000 1600 - street 46 00000100000 1600 ____
    like_doma = '{}__'.format(region + subtotal_region + street)
    like_address = '{}'.format(region + subtotal_region + street)
    doma = Doma.query.filter(Doma.code.like(like_doma)).order_by(Doma.name).all()
    altnames = altnames_kladr(like_address)
    address = Street.query.filter(Street.code.like(like_address)).all()
    template_context = dict(chek='doma', doma=doma, address=address, altnames=altnames)
    return render_template('kladr/kladr_street.html', **template_context)

@kladr.route('/distrikt/<region>/<subtotal_region>/<cheek>')  # <level> имя параметра
def kladr_distrikt(region, subtotal_region, cheek):
    print('kladr_distrikt')
    if int(subtotal_region[-2:]) >= 1 and int(subtotal_region[-2:]) <= 50:
        subtotal_region = subtotal_region[:-2] + '00'
    if cheek == 'c':
        # region = 46; subtotal_region = 00400100000;
        like_street = '{}____'.format(region + subtotal_region)
        like_settlement = '{}_____'.format(region + subtotal_region[:6])
        street = Street.query.filter(Street.code.like(like_street)).order_by(Street.name).all()
        notquery = '{}'.format(region + subtotal_region)
        settlement = Kladr.query.filter(Kladr.code.like(like_settlement), Kladr.code != notquery).order_by(Kladr.name).all()
        altnames = altnames_kladr(notquery)
        address = Kladr.query.filter(Kladr.code.like(notquery)).all()
        template_context = dict(chek='citi', street=street, settlement=settlement, address=address, altnames=altnames)
    if cheek == 's':
        # region = 46; subtotal_region = 00400100000;
        like_street = '{}____'.format(region + subtotal_region)
        like_doma = '{}______'.format(region + subtotal_region)
        street = Street.query.filter(Street.code.like(like_street)).order_by(Street.name).all()
        doma = Doma.query.filter(Doma.code.like(like_doma)).order_by(Doma.name).all()
        notquery = '{}'.format(region + subtotal_region)
        address = Kladr.query.filter(Kladr.code.like(notquery)).all()
        altnames = altnames_kladr(notquery)
        template_context = dict(chek='settlement', street=street, doma=doma, address=address, altnames=altnames)

    return render_template('kladr/kladr_distrikt.html', **template_context)

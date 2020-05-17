from sqlalchemy.orm import relationship

from app import db




class Kladr(db.Model):
    __bind_key__ = 'kladr'
    __tablename__ = 'kladr'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    socr = db.Column(db.String(10), db.ForeignKey('socrbase.scname'))
    code = db.Column(db.String(13))
    index = db.Column(db.String(6))
    gninmb = db.Column(db.String(4))
    uno = db.Column(db.String(4))
    ocatd = db.Column(db.String(11))
    status = db.Column(db.String(1))
    socrname = relationship('Socrbase')

    def __init__(self, *args, **kwargs):
        super(Kladr, self).__init__(*args, **kwargs)

    def __repr__(self):  #reprezentaishen определяет представление класса
        return 'name:{}, socr:{}, code:{}, index:{}, gninmb:{}, uno:{}, ocatd:{}, status:{}'.format(self.name, self.socr, self.code, self.index, self.gninmb, self.uno, self.ocatd, self.status)



class Street(db.Model):
    __bind_key__ = 'kladr'
    __tablename__ = 'street'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    socr = db.Column(db.String(10), db.ForeignKey('socrbase.scname'))
    code = db.Column(db.String(17))
    index = db.Column(db.String(6))
    gninmb = db.Column(db.String(4))
    uno = db.Column(db.String(4))
    ocatd = db.Column(db.String(11))
    socrname = relationship('Socrbase')

    def __init__(self, *args, **kwargs):
        super(Street, self).__init__(*args, **kwargs)

    def __repr__(self):  #reprezentaishen определяет представление класса
        return 'name:{}, socr:{}, code:{}, index:{}, gninmb:{}, uno:{}, ocatd:{}'.format(self.name, self.socr, self.code, self.index, self.gninmb, self.uno, self.ocatd)



class Doma(db.Model):
    __bind_key__ = 'kladr'
    __tablename__ = 'doma'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    korp = db.Column(db.String(10))
    socr = db.Column(db.String(10))
    code = db.Column(db.String(19))
    index = db.Column(db.String(6))
    gninmb = db.Column(db.String(4))
    uno = db.Column(db.String(4))
    ocatd = db.Column(db.String(11))

    def __init__(self, *args, **kwargs):
        super(Doma, self).__init__(*args, **kwargs)

    def __repr__(self):  #reprezentaishen определяет представление класса
        return 'name:{}, korp:{}, socr:{}, code:{}, index:{}, gninmb:{}, uno:{}, ocatd:{}'.format(self.name, self.korp, self.socr, self.code, self.index, self.gninmb, self.uno, self.ocatd)



class Altnames(db.Model):
    __bind_key__ = 'kladr'
    __tablename__ = 'altnames'
    id = db.Column(db.Integer, primary_key=True)
    oldcode = db.Column(db.String(19))
    newcode = db.Column(db.String(19))
    level = db.Column(db.String(1))


    def __init__(self, *args, **kwargs):
        super(Altnames, self).__init__(*args, **kwargs)

    def __repr__(self):  #reprezentaishen определяет представление класса
        return 'oldcode:{}, newcode:{}, level:{}'.format(self.oldcode, self.newcode, self.level)



class Namemap(db.Model):
    __bind_key__ = 'kladr'
    __tablename__ = 'namemap'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(19))
    name = db.Column(db.String(250))
    shname = db.Column(db.String(40))
    scname = db.Column(db.String(10))


    def __init__(self, *args, **kwargs):
        super(Namemap, self).__init__(*args, **kwargs)

    def __repr__(self):  #reprezentaishen определяет представление класса
        return 'code:{}, name:{}, shname:{}, scname:{}'.format(self.code, self.name, self.shname, self.scname)



class Socrbase(db.Model):
    __bind_key__ = 'kladr'
    __tablename__ = 'socrbase'
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(5))
    scname = db.Column(db.String(10))
    socrname = db.Column(db.String(29))
    kod_t_st = db.Column(db.String(3))


    def __init__(self, *args, **kwargs):
        super(Socrbase, self).__init__(*args, **kwargs)

    def __repr__(self):  #reprezentaishen определяет представление класса
        return 'level:{}, scname:{}, socrname:{}, kod_t_st:{}'.format(self.level, self.scname, self.socrname, self.kod_t_st)


class Flat(db.Model):
    __bind_key__ = 'kladr'
    __tablename__ = 'flat'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    code = db.Column(db.String(23))
    index = db.Column(db.String(6))
    gninmb = db.Column(db.String(4))
    uno = db.Column(db.String(4))
    np = db.Column(db.String(4))

    def __init__(self, *args, **kwargs):
        super(Flat, self).__init__(*args, **kwargs)

    def __repr__(self):  #reprezentaishen определяет представление класса
        return 'name:{}, code:{}, index:{}, gninmb:{}, uno:{}, np:{}'.format(self.name, self.code, self.index, self.gninmb, self.uno, self.np)

from app import db




class Kladr(db.Model):
    __bind_key__ = 'kladr'
    __tablename__ = 'kladr'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    socr = db.Column(db.String(10))
    code = db.Column(db.String(13))
    index = db.Column(db.String(6))
    gninmb = db.Column(db.String(4))
    uno = db.Column(db.String(4))
    ocatd = db.Column(db.String(11))
    status = db.Column(db.String(1))

    def __init__(self, *args, **kwargs):
        super(Kladr, self).__init__(*args, **kwargs)

    def __repr__(self):  #reprezentaishen определяет представление класса
        return 'name:{}, socr:{}, code:{}, index:{}, gninmb:{}, uno:{}, ocatd:{}, status:{}'.format(self.name, self.socr, self.code, self.index, self.gninmb, self.uno, self.ocatd, self.status)

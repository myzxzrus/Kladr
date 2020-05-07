from app import db
from datetime import datetime
import re

def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


class Post(db.Model):
    __bind_key__ = 'myzxzrus'
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):  #reprezentaishen определяет представление класса
        return '<Post id: {}, title: {}>'.format(self.id, self.title)



class Street_new(db.Model):
    __bind_key__ = 'myzxzrus'
    __tablename__ = 'street_new'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    socr = db.Column(db.String(10))
    code = db.Column(db.String(17))
    index = db.Column(db.String(6))
    gninmb = db.Column(db.String(4))
    uno = db.Column(db.String(4))
    ocatd = db.Column(db.String(11))

    def __init__(self, *args, **kwargs):
        super(Street_new, self).__init__(*args, **kwargs)

    def __repr__(self):  #reprezentaishen определяет представление класса
        return 'name:{}, socr:{}, code:{}, index:{}, gninmb:{}, uno:{}, ocatd:{}'.format(self.name, self.socr, self.code, self.index, self.gninmb, self.uno, self.ocatd)


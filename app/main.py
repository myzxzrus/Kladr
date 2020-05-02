from app import app
from app import db
from posts.blueprint import posts
from kladr.blueprint_kladr import kladr
import view


app.register_blueprint(posts, url_prefix='/blog')
app.register_blueprint(kladr, url_prefix='/kladr')

if __name__ == '__main__':
    app.run()


#  Точка входа в приложение.

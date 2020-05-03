from flask import Blueprint
from flask import render_template
# from models_kladr import Kladr
from models import Post

posts = Blueprint('posts', __name__, template_folder='templates')

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


@posts.route('/')
def index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)



@posts.route('/<slug>')  # <slug> имя параметра
def post_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    return render_template('posts/post_detail.html', post=post)

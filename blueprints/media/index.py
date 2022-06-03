from flask import Blueprint,render_template

bl=Blueprint('index',__name__,url_prefix='/')

@bl.route('/')
def index():
    return render_template('media/index.html',scroll_images=['https://static.runoob.com/images/mix/img_nature_wide.jpg','https://static.runoob.com/images/mix/img_fjords_wide.jpg'])
from flask import Blueprint,render_template

bl=Blueprint('setting',__name__,url_prefix='/setting')

@bl.route('/')
def index():

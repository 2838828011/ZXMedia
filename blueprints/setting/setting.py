from flask import Blueprint,render_template
from core.model.sqlite_queue import sqlite_data

bl=Blueprint('setting',__name__,url_prefix='/setting')

@bl.route('/')
def index():
    return render_template('setting/setting_index.html')

@bl.route('/managesearchpath')
def manage_search_path():
    search_paths=sqlite_data.cur_execute('SELECT * FROM SearchPath',use_dic=True)
    return render_template('setting/manage_search_path.html', search_paths=search_paths)
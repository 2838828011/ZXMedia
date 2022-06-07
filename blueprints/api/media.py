from flask import Blueprint, request, url_for, render_template, redirect
from core.model.sqlite_queue import sqlite_data

bl = Blueprint('api_media', __name__, url_prefix='/api/media')


@bl.route('/removesearchpath', methods=['GET'])
def remove_search_path():
    args = request.args
    path_name = args.get('name')
    print(path_name)
    if path_name is None:
        return render_template('error/main_error.html', error_message='未输入媒体库名称')
    elif sqlite_data.select('SearchPath', f'where name="{path_name}"') is None:
        return render_template('error/main_error.html', error_message='不存在该媒体库')
    else:
        sqlite_data.cur_execute('DELETE FROM SearchPath WHERE name=?', (path_name,))
        return redirect(url_for('setting.manage_search_path'))


@bl.route('/removesearchpath', methods=['POST'])
def add_new_path_post():
    get_form=request.form
    if get_form.get('force') == 'on':
        sqlite_data.insert('SearchPath',
                           name=get_form.get('name'),
                           path=get_form.get('path'),
                           type=get_form.get('type')
                           )
        return redirect(url_for('setting.manage_search_path'))
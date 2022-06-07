from flask import Blueprint, render_template, url_for, request,abort
from core.model.sqlite_queue import sqlite_data

bl = Blueprint('media', __name__, url_prefix='/media')


@bl.route('/')
def index():
    show_tv = {}
    for media_type, url in [('tv', url_for('media.tv_index'))]:
        get = sqlite_data.cur_execute('SELECT name FROM SearchPath where type=?', (media_type,))
        if media_type not in show_tv:
            show_tv[(media_type, url)] = []
        for i in get:
            show_tv[(media_type, url)].append(i[0])
    print(show_tv)
    return render_template('media/media.html', show_tv=show_tv)


@bl.route('/tv')
def tv_index():
    args = request.args
    media_type = args.get('type')
    if media_type == '' or media_type is None:
        search_path_name = sqlite_data.cur_execute('SELECT name from SearchPath')
        show_tv = {}
        for each_search_path_name, in search_path_name:
            show_tv[each_search_path_name] = []
            episode_thing = sqlite_data.cur_execute('SELECT * FROM EpisodeMedia where father_search_path=?',
                                                    (each_search_path_name,))
            for i in episode_thing:
                if i[2] is None:  # 如果没有name
                    name = f'{i[1]} 第{i[5]}季 第{i[6]}集'  # 自动生成剧集名称
                else:
                    name = i[2]
                show_tv[each_search_path_name].append(
                    {
                        'name': name,
                        'id': i[3],
                        'cover_picture_id': i[7] if i[7] is not None else ''
                    }
                )
            print(show_tv)
        return render_template('media/tv/tv_show_all_episode.html', show_tv=show_tv)
    elif media_type == 'all':
        show_tv = []
        tv_names = sqlite_data.cur_execute('SELECT tv_name,tv_cover_picture_id FROM EpisodeMedia GROUP BY season,tv_name')
        for tv_name,tv_cover_picture_id in tv_names:
            if tv_cover_picture_id is None:
                tv_cover_picture_id=''
            show_tv.append((tv_name,tv_cover_picture_id))
            print(tv_name)
        return render_template('media/tv/tv_show_all.html', show_tv=show_tv)

    elif media_type == 'episode':
        tv_name = args.get('name')
        episode_id = args.get('id')
        if episode_id is not None:
            episode_detail = sqlite_data.select(table_name='EpisodeMedia', other=f'where id="{episode_id}" ORDER BY episode')
            if episode_detail is None:
                return  render_template('error/main_error.html',error_message='episode_id不存在')
            print(episode_detail[0])
            episode_detail=list(episode_detail[0]) #取第一个出来（其实就一个）
            episode_detail[7] = '' if episode_detail[7] is None else episode_detail[7]
            return render_template('media/episode/episode.html',show_tv=episode_detail)
        elif tv_name is not None:
            episode_detail = sqlite_data.cur_execute('SELECT tv_name,name,id,season,episode,cover_picture_id,tv_cover_picture_id FROM EpisodeMedia where tv_name=? ORDER BY season,episode',(tv_name,))
            if episode_detail is None:
                return render_template('error/main_error.html', error_message='tv_name不存在')
            print(episode_detail)
            show_tv=[]
            for tv_name,name,episode_id,season,episode,cover_picture,tv_cover_picture in episode_detail:
                name=name if name is not None else f'{tv_name} 第{season}季 第{episode}集'
                cover_picture = cover_picture if cover_picture is not None else ''
                tv_cover_picture=tv_cover_picture if tv_cover_picture is not None else ''
                show_tv.append(
                    {
                        'tv_name':tv_name,
                        'name':name,
                        'episode_id':episode_id,
                        'season':season,
                        'episode':episode,
                        'cover_picture':cover_picture,
                        'tv_cover_picture':tv_cover_picture
                    }
                )
            print(show_tv)
            return render_template('media/episode/tv.html',show_tv=show_tv)
        else:
            return render_template('error/main_error.html', error_message='tv_name丢失')

from core.model.sqlite_queue import sqlite_data
from core.model.group import TVGroup
from core.function.file import get_dirs, get_files
from os.path import split as split_file_name
from core.function.regular_xpression import find as re_find


def search_from_tv(search_path_name, path: str) -> 'TVGroup':
    season_re = [
        '[Ss](\d)',
        'Season(\d)'
    ]
    episode_re = [
        'S\d{0,3}E(\d{0,3})',
        '\[[Ee][Pp]{0,1}(\d{1,3})\]',
        '第(\d{1,3})集',
        '\[(\d{1,3})\]'
    ]
    temp = TVGroup(search_path_name, split_file_name(path)[-1])
    seasons = get_dirs(path)
    for each_season in seasons:
        season_number = re_find(season_re, split_file_name(each_season)[-1])
        if season_number is not None:
            season_number = int(season_number.group(1))
            temp.add_season(season_number)
            for each_file in get_files(each_season):
                episode_number = re_find(episode_re, split_file_name(each_file)[-1])
                if episode_number is not None:
                    temp.add_episode(season_number, episode_number.group(1), each_file)
    return temp


def search_from_movie(path):
    pass


def search_from_picture(path):
    pass


def search():
    video = sqlite_data.select('SearchPath')
    for i in video:
        if i[1] == 'tv':
            for each_path in get_dirs(i[2]):  # 获取剧集媒体库下方所有的文件夹
                tv_group = search_from_tv(i[0], each_path)
                # print(tv_group.data)
                tv_group.add_to_database(sqlite_data)


if __name__ == '__main__':
    search()

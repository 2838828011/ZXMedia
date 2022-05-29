from core.model.sqlite_queue import sqlite_data
from core.model.group import TVGroup
from core.function.file import get_dirs,get_files
from os.path import split as split_file_name,splitext
import re

def search_from_tv(path):
    temp=TVGroup(split_file_name(path)[-1])
    seasons=get_dirs(path)
    for each_season in seasons:
        season_number=re.search('[Ss](\d)|Season(\d)',split_file_name(each_season)[-1])
        if season_number is not None:
            season_number=int(season_number.group()[-1])
            temp.add_season(season_number)
            for each_file in get_files(each_season):
                episode_number = re.search('S\d{0,3}E(\d{0,3})',split_file_name(each_file)[-1])
                if episode_number is not None:
                    temp.add_episode(season_number,episode_number.group(1),each_file)
    print(temp.data)
def search_from_movie(path):
    pass

def search_from_picture(path):
    pass

def search():
    video=sqlite_data.select('SearchPath')
    for i in video:
        if i[0] == 'tv':
            for each_path in get_dirs(i[1]): #获取下方所有的
                search_from_tv(each_path)

if __name__ == '__main__':
    search()
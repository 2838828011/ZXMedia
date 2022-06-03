import re
from core.model.sqlite_queue import SqliteQueue
from core.function.new_id import get_id1
class TVGroup:
    def __init__(self, tv_name: None or str = None):
        self.tv_name = tv_name
        self.__episodes = []

    def add_season(self,season_number:int):
        if self.__find_season(season_number=season_number) is None:
            self.__episodes.append(
                {
                    'season':season_number,
                    'episodes':{}
                }
            )
        else:
            raise KeyError('season_number重复')

    def __find_season(self,season_number:int):
        for _ in self.__episodes:
            if _.get('season') == season_number:
                return _.get('episodes')
        return None

    def add_episode(self,searson_number:int,episode_number,file_path):
        episode_dic = self.__find_season(season_number=searson_number)
        if episode_dic is None:
            ValueError('不存在season_number',searson_number)
        if isinstance(episode_number,str):
            searson_number=re.search('OP\d{0,2}|ED\d{0,2}|\d{1,2}\.5|\d{1,2}',episode_number)#'13.21'->13
            if searson_number is None:
                raise ValueError('episode_number错误')
            else:
                episode_dic[searson_number.group()]=file_path
        else:
            raise ValueError('episode_number应为str')

    @property
    def data(self):
        return {
            'tv_name':self.tv_name,
            'episodes':self.__episodes
        }


    def add_to_database(self,db:'SqliteQueue'):
        name = self.tv_name
        if isinstance(db,SqliteQueue):
            for i in self.__episodes:
                season_number=i.get('season')
                episodes=i.get('episodes')
                for _ in episodes:
                    db.insert('EpisodeMediaTemp',
                                season=season_number,
                                episode=_,
                                path=episodes[_],
                                id=get_id1(),
                                tv_name=name
                              )
            db.cur_execute('INSERT INTO EpisodeMedia '
                           'SELECT * from EpisodeMediaTemp '
                           'where path not in (SELECT path FROM EpisodeMedia)'
                           )
            db.cur_execute('DELETE from EpisodeMedia '
                           'where path not in (SELECT path FROM EpisodeMediaTemp)'
                           )





if __name__ == '__main__':
    a=TVGroup()
    a.add_season(1)
    a.add_episode(1,'S0E11','fwaf')
    print(a.data)
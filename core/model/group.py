import re
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

if __name__ == '__main__':
    a=TVGroup()
    a.add_season(1)
    a.add_episode(1,'S0E11','fwaf')
    print(a.data)
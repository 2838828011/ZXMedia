CREATE table if not exists config ( --本项目有两种config,一种不能直接修改，在'./data/config.py'修改，另一种在数据库里
    key TEXT UNIQUE NOT NULL ,
    value TEXT NOT NULL
);
CREATE TABLE if not exists MediaData ( --媒体数据库，存放元数据
    id TEXT UNIQUE NOT NULL ,
    season_number TEXT , --可选选项，剧集的时候填
    episode_number TEXT , --同上
    score TEXT --评分

);
CREATE TABLE if not exists SearchPath (
    type TEXT NOT NULL ,
    path TEXT UNIQUE NOT NULL
);
CREATE TABLE if not exists Series (
    id TEXT UNIQUE NOT NULL
);
CREATE TABLE if not exists CheckedMedia ( --搜索好了的文件放这里
    type TEXT NOT NULL ,
    name TEXT NOT NULL ,
    path TEXT NOT NULL ,
    media_data_id TEXT ,
    series_id TEXT
);
CREATE TABLE if not exists MediaTemp AS SELECT * FROM CheckedMedia WHERE 1=0 --先把搜索到到的文件放里面，新增的文件加入，不存在的文件删除

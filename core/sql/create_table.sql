DROP TABLE if exists EpisodeMediaTemp;
CREATE table if not exists config ( --本项目有两种config,一种不能直接修改，在'./data/config.py'修改，另一种在数据库里
    key TEXT UNIQUE NOT NULL ,
    value TEXT NOT NULL
);
CREATE TABLE if not exists MediaData ( --媒体数据库，存放元数据
    id TEXT UNIQUE NOT NULL ,
    score TEXT --评分

);
CREATE TABLE if not exists SearchPath (
    name TEXT NOT NULL ,
    type TEXT NOT NULL ,
    path TEXT UNIQUE NOT NULL ,
    icon TEXT
);
CREATE TABLE if not exists Series (
    id TEXT UNIQUE NOT NULL
);

CREATE TABLE if not exists EpisodeMedia (
    father_search_path TEXT NOT NULL ,
    tv_name TEXT NOT NULL ,
    name TEXT ,
    id TEXT NOT NULL UNIQUE ,
    path TEXT NOT NULL UNIQUE ,
    season TEXT NOT NULL ,
    episode TEXT NOT NULL ,
    cover_picture_id TEXT ,
    tv_cover_picture_id TEXT
);
CREATE TABLE if not exists EpisodeMediaTemp AS SELECT * FROM EpisodeMedia WHERE 1=0; --先把搜索到到的文件放里面，新增的文件加入，不存在的文件删除
CREATE TABLE if not exists Resource (
    id TEXT NOT NULL UNIQUE ,
    path TEXT NOT NULL UNIQUE
)
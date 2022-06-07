import sqlite3
from queue import Queue
from data.config import database_path,init_table_path
class SqliteQueue(Queue):  # 君子式队列
    def __init__(self, sqlite_path=''):
        super(SqliteQueue, self).__init__(1)
        self.__sqlite_path = sqlite_path
        temp = sqlite3.connect(self.__sqlite_path)
        temp.close()
        self.put(1)

    def get_db(self):
        self.get()
        return sqlite3.connect(self.__sqlite_path)

    def close_db(self, db):
        db.close()
        self.put(1)

    def insert(self, table_name: str, **values):
        db = self.get_db()
        cur = db.cursor()
        command = f"insert into {table_name}({','.join(list(values.keys()))}) values({','.join(['?' for i in range(len(values))])})"
        cur.execute(command, tuple(values.values()))
        db.commit()
        self.close_db(db)

    def delete(self, table_name, other):
        pass

    def updata(self,table_name,other,**keys):
        db=self.get_db()
        cur=db.cursor()
        command=f'UPDATE {table_name} SET {",".join([i+" = ?" for i in keys])} {other}'
        cur.execute(command,tuple(keys.values()))
        db.commit()
        self.close_db(db)


    def select(self, table_name, other=''):
        db = self.get_db()
        cur = db.cursor()
        command = f"select * from {table_name} {other}"
        cur.execute(command)
        temp = cur.fetchall()
        self.close_db(db)
        return temp

    def create_table(self, table_name, **keys):
        db = self.get_db()
        command = f'create table if not exists {table_name}({",".join([i + " " + keys[i] for i in keys])})'
        print(command)
        self.close_db(db)

    def execute_from_file(self, file_path):
        db = self.get_db()
        with open(file_path, 'r', encoding='utf-8') as f:
            db.executescript(f.read())
        db.commit()
        self.close_db(db)

    def cur_execute(self, command, values=None ,use_dic=False):
        def dict_factory(cursor, row):
            d = {}
            for idx, col in enumerate(cursor.description):
                d[col[0]] = row[idx]
            return d
        db = self.get_db()
        if use_dic is True:
            db.row_factory = dict_factory
        cur = db.cursor()
        if values is None:
            cur.execute(command)
        else:
            cur.execute(command, values)
        temp=cur.fetchall()
        db.commit()
        self.close_db(db)
        return temp


sqlite_data = SqliteQueue(database_path)
sqlite_data.execute_from_file(init_table_path)
#sqlite_data.cur_execute('INSERT OR IGNORE INTO SearchPath(type, path) VALUES (?,?)',('tv','/Volumes/文件1/视频/剧集/动漫'))
sqlite_data.cur_execute('INSERT OR IGNORE INTO SearchPath(name,type, path) VALUES (?,?,?)',('本地测试','tv','/Users/zhangbeiyuan/Downloads'))
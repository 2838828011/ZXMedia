from core.model.sqlite_queue import sqlite_data
def get_pic(resource_id:str or None) -> None or str:
    print(resource_id)
    if  resource_id is None:
        return None
    pic_path=sqlite_data.cur_execute('SELECT path FROM Resource WHERE id=?',(resource_id,))
    if pic_path is None:
        return pic_path
    else:
        return pic_path[0]


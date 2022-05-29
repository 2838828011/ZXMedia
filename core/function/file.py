from os import listdir
from os.path import isfile,isdir
def get_child(path:str) -> tuple:
    if path[-1] !='/':path+='/'
    files=[];dirs=[]
    for i in listdir(path):
        i=path+i
        if isfile(i) is True:
            files.append(i)
        elif isdir(i) is True:
            dirs.append(i)
    return files,dirs

def get_dirs(path:str) -> list:
    return get_child(path)[1]

def get_files(path:str) -> list:
    return get_child(path)[0]

if __name__ == '__main__':
    print(get_dirs('/Users/zhangbeiyuan/Downloads'))

import re
def find(re_list:list,string:str) -> 're.Match' or None:
    '''

    :param re_list: 正则表达式
    :param string: 匹配的字符
    :return: 返回匹配的字符
    '''

    for i in re_list:
        compile=re.compile(i)
        temp=re.search(compile,string)
        if temp is not None:
            return temp

if __name__ == '__main__':
    r = [
        '\[[Ee][Pp]{0,1}(\d{1,3})\]',
        '第(\d{1,3})集'
    ]
    name = "[诸神字幕组] jin ji de jv ren [s01][e01]"
    print(find(r,name).group(1))
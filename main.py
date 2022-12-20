import json
import time

def get_con(path):

    lists = []
    with open(path+'.json', 'r', encoding='utf-8')as f:
        for index, i in enumerate(json.loads(f.read())['data']['Questions']):
            Option_lists = i['Option']
            total_que = f'{index+1} {i["Question"]}'
            lists.append(total_que)
            for j in Option_lists:
                key = j['Key']
                value = j['Value']
                new_option = f'{key} {value}'
                lists.append(new_option)
        return lists


def saved_doc(name, con_list):
    with open(f'{name}.txt', 'w', encoding='utf-8')as f:
        for i in con_list:
            f.write(i+'\n')


def main(name, path):
    content_list = get_con(path)
    saved_doc(name, content_list)


if __name__ == '__main__':
    path = input('请输入当前目录下json文件的名称: ')
    name = input('请输入要生成的赛事星题目的名称: ')
    start = time.time()
    main(name, path)
    print('Progrem Finish\n', f'共耗时{time.time()-start}')
    
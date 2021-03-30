'''
@Author: lil_T 117
@Date  :  3:09 下午
'''

'''
删除文件中包含关键字的行
path_o：源文件地址
path_n：删除匹配行后文件
keywords：关键字list
'''
def del_lines(path_o, path_n, keywords):
    with open(path_o, 'r') as r:
        lines = r.readlines()
    with open(path_n, 'w') as w:
        for l in lines:
            flag = 0
            for x in range(len(keywords)):
                if keywords[x] in l:
                    flag += 1
            if not flag:
                w.write(l)

path_o = "/Users/zhangtong/Downloads/root-2021-03-24-90 2.log"
path_n = "/Users/zhangtong/PycharmProjects/117_pj/tools/root-2021-03-24-90-1.log"
keywords = ["围栏产品","request=","time cost"]

del_lines(path_o, path_n, keywords)
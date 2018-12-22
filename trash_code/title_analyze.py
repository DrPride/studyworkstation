# -*- coding: utf-8 -*-
''' 
    this file is designed to analyze the
    title and get the necessary information
    such as the delivery time, the reason of delivery 
    and so on 
'''

# -*- coding: utf-8 -*-
import jieba 

def time_train():
    for i in range(1,13):
        suggest_str = str(i) + '月'
        jieba.suggest_freq(suggest_str, True)

def word_train(add_list = []):
    # add_list is a peremeter for you easily add the word you don't want to seperate
    str_list = ['国家奖学金', '爱心助学金', '勤工助学工资']
    str_list.extend(add_list)
    #print(type(str_list), str_list)
    for i in str_list:
        jieba.suggest_freq(i, True)

def string_analyze(title):
    # the str should be the filename of the upload file.
    # rtype dict{'time':time,'id': id, 'reson': reason ...}
    seg_list = jieba.cut(title)
    info_list = ['time','id', 'reson']
    seg_list = list(seg_list)
    return_dict = {}
    # print(seg_list)
    if len(seg_list) != len(info_list):
        print('There is a problem', seg_list)
        return False
    for i in range(len(seg_list)):
        return_dict[info_list[i]] = seg_list[i]
    return return_dict 
        

def Titile_Analyze(title, add_list = []):
    time_train()
    word_train(add_list)
    return string_analyze(title)

if __name__ == '__main__':
    #main()
    time_train()
    word_train()
    # standard input: "time-id-reson"
    print(string_analyze('4月本专科勤工助学工资'))


    
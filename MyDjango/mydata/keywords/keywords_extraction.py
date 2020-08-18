#-*- encoding:utf-8 -*-
from __future__ import print_function

import sys
from imp import reload
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass
from textrank4zh import TextRank4Keyword

# 定义关键词抽取函数
def keywords_extraction(text):
    tr4w = TextRank4Keyword()
    tr4w.analyze(text=text, lower=True, window=2)
        # 在这里输出关键词
    keywords = ""
    print('关键词：')
    for item in tr4w.get_keywords(3, word_min_len=1):
        print(item.word, item.weight)
        keywords = keywords+item.word+','
    print(keywords)
    return keywords


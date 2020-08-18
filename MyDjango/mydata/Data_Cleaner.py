#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import json
import re
import MySQLdb
import io
from mydata.keywords.keywords_extraction import keywords_extraction
from mydata.levenshtein import levenshtein
import string
import nltk
import sys
import os
import sys

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class Data_Cleaner:

    def compound_word_split(self, compound_word):
        """
        Split a given compound word(string) and return list of words in given compound_word
        Ex: compound_word='pyTWEETCleaner' --> ['py', 'TWEET', 'Cleaner']
        """
        matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', compound_word)
        return [m.group(0) for m in matches]

    def remove_non_ascii_chars(self, text):
        """
        return text after removing non-ascii characters i.e. characters with ascii value >= 128
        """
        return ''.join([w if ord(w) < 128 else ' ' for w in text])

    def remove_hyperlinks(self, text):
        """
        return text after removing hyperlinks
        """
        results = re.compile(r'http://[a-zA-Z0-9.?/&=:]*', re.S)
        clean_data = results.sub("", text)

        #clean_data = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', text, flags=re.MULTILINE)
        return (clean_data)

      #  return ' '.join([w for w in text.split(' ') if not 'http' in w])

    def get_cleaned_text(self, text):
        """
        return cleaned text(string) for provided tweet text(string)
        """

        cleaned_text=text.replace('  ','')

        cleaned_text = re.sub(r'<[^>]+>', '', cleaned_text, flags=re.MULTILINE)


        cleaned_text = self.remove_hyperlinks(cleaned_text)

        cleaned_text = cleaned_text.replace('#', 'HASHTAGSYMBOL').replace('@', 'ATSYMBOL').replace('$', 'DOLLARSYMBOL')  # to avoid being removed while removing punctuations

        return cleaned_text

    def get_cleaned_zhihu(self, data):
        cleaned_data = {}

        answer_length = 0

        for key in data:
            if ("answer" in key and re.search(r'\d', key)):
                answer_length = answer_length + 1

        cleaned_data['question id'] = data['question id']
        cleaned_data['question'] = self.get_cleaned_text(data['question'])
        cleaned_data['detail'] = self.get_cleaned_text(data['detail'])
        cleaned_data['answer count'] = answer_length
        cleaned_data['follower count'] = data['follower count']


        if int(cleaned_data['answer count'])>0:
            for i in range(0, answer_length):
                cleaned_data['answer' + str(i)] = {}
                #            print(data['answer'+str(i)]['answer'])
                answers = ""
                for answertxt in data['answer' + str(i)]['answer']:
                    answers = answers + answertxt

                comment_length=0
                for key in data['answer' + str(i)]:
                    if ("comment" in key and re.search(r'\d', key)):
                        comment_length = comment_length + 1

                print(answers)
                cleaned_data['answer' + str(i)]['answer'] = self.get_cleaned_text(answers)
                cleaned_data['answer' + str(i)]['answer author'] = data['answer' + str(i)]['answer author']
                cleaned_data['answer' + str(i)]['voteup count'] = data['answer' + str(i)]['voteup count']
                cleaned_data['answer' + str(i)]['create_time'] = data['answer' + str(i)]['create_time']
                cleaned_data['answer' + str(i)]['thanks count'] = data['answer' + str(i)]['thanks count']
                cleaned_data['answer' + str(i)]['updated time'] = data['answer' + str(i)]['updated time']
                cleaned_data['answer' + str(i)]['comment count'] = comment_length

                if int(comment_length) > 0:
                    for j in range(0, int(comment_length)):
                        cleaned_data['answer' + str(i)]['comment' + str(j)] = {}
                        cleaned_data['answer' + str(i)]['comment' + str(j)]['content'] = self.get_cleaned_text(data['answer' + str(i)]['comment' + str(j)]['content'])
                        cleaned_data['answer' + str(i)]['comment' + str(j)]['comment author'] = data['answer' + str(i)]['comment' + str(j)]['comment author']
                        cleaned_data['answer' + str(i)]['comment' + str(j)]['create_time'] = data['answer' + str(i)]['comment' + str(j)]['create_time']
                        cleaned_data['answer' + str(i)]['comment' + str(j)]['vote count'] = data['answer' + str(i)]['comment' + str(j)]['vote count']

        return cleaned_data

    def open_sql(self, input_file):
        # 打开数据库连接
        db = MySQLdb.Connect("10.1.48.211", "root", "123456", "wrj_db",charset="utf8")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        question_id=7357
        answer_id = 122130
        comment_id = 587519

        files = os.listdir(input_file)

        for f in files:
            if os.path.isfile(input_file+ '/' + f):
                input="zhihu/新型冠状病毒肺炎5/" + f
                if not os.path.getsize(input):
                    print(input+"is empty!")
                else:
                    with open(input, 'r', encoding='utf8')as fp:

                        data = json.load(fp)
                        cleaned_data = self.get_cleaned_zhihu(data)

                        print(cleaned_data)
                        date_number=str(f)[0:10]

                        question_title = cleaned_data['question']
                        question_detail = cleaned_data['detail']
                        question_follower_count = cleaned_data['follower count']
                        question_answer_count = cleaned_data['answer count']
                        question_create_time=date_number
                        # 定义插入语句
                        if int(question_answer_count) > 0:
                            question_id = question_id + 1
                            insert_sql1 = "insert into zhihu_question_5(id,question_title,follower_count,detail,total_answer,created_time) values('%s','%s','%s','%s','%s','%s') " % ( question_id, question_title, question_follower_count, question_detail,question_answer_count, question_create_time)

                            # 执行插入语句
                            try:
                                cursor.execute(insert_sql1)
                                # 提交到数据库执行
                                db.commit()
                                print('%d条记录插入成功' % cursor.rowcount)

                                if int(question_answer_count) > 0:
                                    for i in range(0, int(question_answer_count)):
                                        # print('进入了answer的for循环')
                                        answer_id = answer_id + 1
                                        answer_content = cleaned_data['answer' + str(i)]['answer']
                                        answer_author = cleaned_data['answer' + str(i)]['answer author']
                                        answer_voteup_count = cleaned_data['answer' + str(i)]['voteup count']
                                        answer_create_time = cleaned_data['answer' + str(i)]['create_time']
                                        answer_thanks_count = cleaned_data['answer' + str(i)]['thanks count']
                                        answer_updated_time = cleaned_data['answer' + str(i)]['updated time']
                                        answer_comment_count = cleaned_data['answer' + str(i)]['comment count']
                                        # print("answer值：" + str(answer_id) + answer_content + answer_author)
                                        if question_detail=="" or len(question_detail)==0 or question_detail.isspace()==True:
                                            distance = levenshtein(answer_content, question_title)
                                        else:
                                            distance = levenshtein(answer_content, question_detail)
                                        keywords = keywords_extraction(answer_content)

                                        # print(keywords)
                                        # print("distance是：" + str(distance))
                                        # 定义插入语句
                                        insert_sql2 = "insert into zhihu_answer_5(id,question_id,author,voted_count,comment_count,content,created_time,updated_time,thanks_count,keywords,relation) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') " % (answer_id, question_id, answer_author, answer_voteup_count,answer_comment_count, answer_content, answer_create_time, answer_updated_time,answer_thanks_count, keywords, distance)

                                        try:
                                            cursor.execute(insert_sql2)
                                            # 提交到数据库执行
                                            db.commit()
                                            print('%d条记录插入成功' % cursor.rowcount)

                                            if int(answer_comment_count) > 0:
                                                for j in range(0, int(answer_comment_count)):
                                                    # print('进入了comment的for循环')
                                                    comment_id = comment_id + 1
                                                    comment_content = cleaned_data['answer' + str(i)]['comment' + str(j)]['content']
                                                    comment_author = cleaned_data['answer' + str(i)]['comment' + str(j)]['comment author']
                                                    comment_time = cleaned_data['answer' + str(i)]['comment' + str(j)]['create_time']
                                                    comment_vote_count = cleaned_data['answer' + str(i)]['comment' + str(j)]['vote count']
                                                    # print("comment值：" + str(comment_id) + comment_content + comment_author)

                                                    # 定义插入语句
                                                    insert_sql3 = "insert into zhihu_comment_5(id,answer_id,content,author,created_time,voted_count) values('%s','%s','%s','%s','%s','%s') " % (comment_id, answer_id, comment_content, comment_author,comment_time, comment_vote_count)

                                                    try:
                                                        cursor.execute(insert_sql3)
                                                        # 提交到数据库执行
                                                        db.commit()
                                                        print('%d条记录插入成功' % cursor.rowcount)
                                                    except:
                                                        # 发生错误回滚
                                                        db.rollback()
                                                        print('sql3插入失败')


                                        except:
                                            # 发生错误回滚
                                            db.rollback()
                                            print('sql2插入失败')


                            except:
                                # 发生错误回滚
                                db.rollback()
                                print('sql1插入失败')


        db.close()
        #fp2.close()




if __name__ == '__main__':

    cd = Data_Cleaner();

    files = ["zhihu/新型冠状病毒肺炎","zhihu/新型冠状病毒肺炎1","zhihu/新型冠状病毒肺炎2","zhihu/新型冠状病毒肺炎3","zhihu/新型冠状病毒肺炎4","zhihu/新型冠状病毒肺炎5"]
    for var in files:
        cd.open_sql(input_file = var)
    print('数据更新成功！')



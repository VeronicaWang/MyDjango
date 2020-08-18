#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import os
import requests
from tqdm import tqdm

from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException
from bs4 import BeautifulSoup
import json
import random

s = requests.session()
s.keep_alive = True


# In[2]:


# login ZhihuClient
client = ZhihuClient()
user='+8618129193602'
pwd='961204yy'
try:
    client.login(user, pwd)
except NeedCaptchaException:
    # 保存验证码并提示输入，重新登录
    with open('a.gif', 'wb') as f:
        f.write(client.get_captcha())
    captcha = input('please input captcha:')
    client.login(user, pwd, captcha)
client.save_token('token.kpl')
# TOKEN_FILE = 'token.pkl'
#
# if os.path.isfile(TOKEN_FILE):
#     client.load_token(TOKEN_FILE)
# else:
#     client.login_in_terminal()
#     client.save_token(TOKEN_FILE)


def save_answer(topic, answer_numbers=0, save_path = 'zhihu'):
    # if not os.path.exists(save_path):
    #     os.mkdir(save_path)
    # topic_path = save_path + '/' + topic.name
    # if not os.path.exists(topic_path):
    #     os.mkdir(topic_path)

    for i,question in zip(tqdm(range(topic.questions_count)),topic.unanswered_questions):
        question_time = time.localtime(question.created_time)
        question_dt = time.strftime("%Y-%m-%d",question_time)
        # 时间筛选

        question_name = question_dt + '-' + question.title
        question_name = question_name.replace('/',' ')
        question_name = question_name.replace('?', '？')
        question_name = question_name.replace('|', ' ')
        question_name = question_name.replace('"', ' “')
        question_name = question_name.replace('*', ' ')
        question_name = question_name.replace('\\', ' ')

        #  定义存储路径

        creatd_month = save_path + '/' +'新型冠状病毒肺炎'+str(int(str(question_dt)[6]) - 1)
        question_json = creatd_month+'/'+ question_name + '.json'


        if os.path.exists(question_json):
            # 同一个问题不处理
            continue

        with open(question_json, 'w',encoding='utf8') as f:
            # question
            items = {}
            items['question id'] = i
            items['question'] = str(question.title)
            items['detail'] = str(question.detail)
            items['answer count'] = str(question.answer_count)
            items['follower count'] = str(question.follower_count)

            a = 0
            # answers
            for answer in question.answers:
                # 时间
                answer_time = time.localtime(answer.created_time)
                answer_year = answer_time.tm_year
                answer_dt = time.strftime("%Y-%m-%d %H:%M:%S",answer_time)
                if answer_year < 2017:
                    continue

                #updated time
                answer_time2 = time.localtime(answer.updated_time)
                answer_ut = time.strftime("%Y-%m-%d %H:%M:%S", answer_time2)


                # 文本内容
                soup = BeautifulSoup(answer.content,'html.parser')
                text = soup.find_all(text=True)
                answer_name = answer_dt + '-' + answer.author.name


                # answer
                items2= {}

                # for line in text:
                items2['answer'] = text
                items2['answer author'] = answer.author.name

                # voteup count
                items2['voteup count'] = str(answer.voteup_count)

                # create time
                items2['create_time'] = answer_dt

                items2['comment count'] = str(answer.comment_count)

                # 评论内容
                x = 0
                for comment in answer.comments:
                    items3 = {}
                    items3['content'] = comment.content
                    items3['comment author'] = comment.author.name
                    comment_time = time.localtime(comment.created_time)
                    comment_dt = time.strftime("%Y-%m-%d %H:%M:%S", comment_time)
                    items3['create_time'] = comment_dt
                    items3['vote count'] = str(comment.vote_count)
                    items2['comment' + str(x)] = items3
                    x += 1

                items2['thanks count'] = str(answer.thanks_count)

                items2['updated time'] = answer_ut

                answer_numbers += 1

                items['answer' + str(a)] = items2
                a += 1

            # print('------------------------')
            f.write(json.dumps(items, indent=2, ensure_ascii=False))

    return answer_numbers

# # Main topic
answer_numbers_all = 0
topic_id = 21239580   #新型冠状肺炎的话题id
#topic_id = 21238418  #新型冠状病毒的话题id
topic = client.topic(topic_id)
topic_children = topic.children


answer_numbers_all += save_answer(topic, answer_numbers_all)
print('answer_numbers_all: ', answer_numbers_all)
for topic_child in topic_children:
    answer_numbers_all += save_answer(topic_child, answer_numbers_all)
    print('answer_numbers_all: ', answer_numbers_all)

print('answer numbers :',answer_numbers_all)





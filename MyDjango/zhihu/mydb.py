from django.http import  HttpResponse
from zhihu import models
import datetime
import json
from django.db.models import Q
class DateEnconding(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.date):
            return o.strftime('%Y/%m/%d')
# 日期形式转换
def DateChange(Date):
    changed_Date = Date.replace('/','-')
    return changed_Date

# 查询数据库操作
def question_search_1():
    list = models.Question_1.objects.all()
    print('month=1')
    response = {}
    response['code'] = 0
    response['msg'] = ""
    data = []
    for var in list:
        question = {}
        question['id'] = var.__dict__['id']
        question['question'] = var.__dict__['question_title']
        question['follower_count'] = var.__dict__['follower_count']
        question['date'] = var.__dict__['created_time']
        question['total_answer'] = var.__dict__['total_answer']
        if (var.__dict__['detail'] == ''):
            str = '无详情内容'
        else:
            str = var.__dict__['detail']
        question['detail'] = str
        data.append(question)
    response['count'] = len(data)
    response['data'] = data
    # print(data)
    response = json.dumps(response, cls=DateEnconding)
    return response

def question_search_2():

    print("month=2")
    list = models.Question_2.objects.all()
    response = {}
    response['code'] = 0
    response['msg'] = ""
    data = []
    for var in list:
        question = {}
        # print(var.__dict__['id'])
        question['id'] = var.__dict__['id']
        question['question'] = var.__dict__['question_title']
        question['follower_count'] = var.__dict__['follower_count']
        question['date'] = var.__dict__['created_time']
        question['total_answer'] = var.__dict__['total_answer']
        if (var.__dict__['detail'] == ''):
            str = '无详情内容'
        else:
            str = var.__dict__['detail']
        question['detail'] = str
        data.append(question)
    response['count'] = len(data)
    response['data'] = data
    response = json.dumps(response, cls=DateEnconding)
    return response
def question_search_3():
    print("month=3")
    list = models.Question_3.objects.all()
    # print(list)
    response = {}
    response['code'] = 0
    response['msg'] = ""
    data = []
    for var in list:
        question = {}
        question['id'] = var.__dict__['id']
        question['question'] = var.__dict__['question_title']
        question['follower_count'] = var.__dict__['follower_count']
        question['date'] = var.__dict__['created_time']
        question['total_answer'] = var.__dict__['total_answer']
        if (var.__dict__['detail'] == ''):
            str = '无详情内容'
        else:
            str = var.__dict__['detail']
        question['detail'] = str
        data.append(question)
    response['count'] = len(data)
    response['data'] = data
    response = json.dumps(response, cls=DateEnconding)
    return response
def question_search_4():
    print("month=3")
    list = models.Question_4.objects.all()
    response = {}
    response['code'] = 0
    response['msg'] = ""
    data = []
    for var in list:
        question = {}
        # print(var.__dict__['id'])
        question['id'] = var.__dict__['id']
        question['question'] = var.__dict__['question_title']
        question['follower_count'] = var.__dict__['follower_count']
        question['date'] = var.__dict__['created_time']
        question['total_answer'] = var.__dict__['total_answer']
        if (var.__dict__['detail'] == ''):
            str = '无详情内容'
        else:
            str = var.__dict__['detail']
        question['detail'] = str
        data.append(question)
    response['count'] = len(data)
    response['data'] = data
    response = json.dumps(response, cls=DateEnconding)
    return response
def question_search_5():
    print("month=5")
    list = models.Question_5.objects.all()
    response = {}
    response['code'] = 0
    response['msg'] = ""
    data = []
    for var in list:
        question = {}
        # print(var.__dict__['id'])
        question['id'] = var.__dict__['id']
        question['question'] = var.__dict__['question_title']
        question['follower_count'] = var.__dict__['follower_count']
        question['date'] = var.__dict__['created_time']
        question['total_answer'] = var.__dict__['total_answer']
        if (var.__dict__['detail'] == ''):
            str = '无详情内容'
        else:
            str = var.__dict__['detail']
        question['detail'] = str
        data.append(question)
    response['count'] = len(data)
    response['data'] = data
    response = json.dumps(response, cls=DateEnconding)
    return response
def question_search_6():
    print("month=6")
    list = models.Question_6.objects.all()
    print(list)
    print("month=5")
    response = {}
    response['code'] = 0
    response['msg'] = ""
    data = []
    for var in list:
        question = {}
        # print(var.__dict__['id'])
        question['id'] = var.__dict__['id']
        question['question'] = var.__dict__['question_title']
        question['follower_count'] = var.__dict__['follower_count']
        question['date'] = var.__dict__['created_time']
        question['total_answer'] = var.__dict__['total_answer']
        if (var.__dict__['detail'] == ''):
            str = '无详情内容'
        else:
            str = var.__dict__['detail']
        question['detail'] = str
        data.append(question)
    response['count'] = len(data)
    response['data'] = data
    response = json.dumps(response, cls=DateEnconding)
    print(response)
    return response


# 查询answer表中具有相同question_id的answer
def answer_post(question_id,total_answer):
    question_id = int(question_id)
    if question_id<=1914 and question_id>=1:
        list = models.Answer_1.objects.filter(question_id=question_id)[:int(total_answer)]
        response = {}
        response['code'] = 0
        data = []
        answer = {}
        # answer_id = list1.__dict__['id']
        # last_answer = int(total_answer)+answer_id
        # list = models.Answer.objects.all()[answer_id:last_answer]
        for var in list:
            answer = {}
            answer['id'] = var.__dict__['id']
            answer['author'] = var.__dict__['author']
            answer['created_time'] = var.__dict__['created_time']
            answer['updated_time'] = var.__dict__['updated_time']
            answer['content'] = var.__dict__['content']
            answer['keywords'] = var.__dict__['keywords']
            answer['thanks_count'] = var.__dict__['thanks_count']
            answer['relation'] = var.__dict__['relation']
            answer['voted_count'] = var.__dict__['voted_count']
            answer['comment_count'] = var.__dict__['comment_count']
            data.append(answer)
        response['count'] = len(data)
        response['data'] = data
        response = json.dumps(response, cls=DateEnconding)
        return response
    if question_id<=2668 and question_id>=1915:
        list = models.Answer_2.objects.filter(question_id=question_id)[:int(total_answer)]
        response = {}
        response['code'] = 0
        data = []
        for var in list:
            answer = {}
            answer['id'] = var.__dict__['id']
            answer['author'] = var.__dict__['author']
            answer['created_time'] = var.__dict__['created_time']
            answer['updated_time'] = var.__dict__['updated_time']
            answer['content'] = var.__dict__['content']
            answer['keywords'] = var.__dict__['keywords']
            answer['thanks_count'] = var.__dict__['thanks_count']
            answer['relation'] = var.__dict__['relation']
            answer['voted_count'] = var.__dict__['voted_count']
            answer['comment_count'] = var.__dict__['comment_count']
            data.append(answer)
        response['count'] = len(data)
        response['data'] = data
        response = json.dumps(response, cls=DateEnconding)
        return response
    if question_id<=5542 and question_id>=2669:
        list = models.Answer_3.objects.filter(question_id=question_id)[:int(total_answer)]
        response = {}
        response['code'] = 0
        data = []
        for var in list:
            answer = {}
            answer['id'] = var.__dict__['id']
            answer['author'] = var.__dict__['author']
            answer['created_time'] = var.__dict__['created_time']
            answer['updated_time'] = var.__dict__['updated_time']
            answer['content'] = var.__dict__['content']
            answer['keywords'] = var.__dict__['keywords']
            answer['thanks_count'] = var.__dict__['thanks_count']
            answer['relation'] = var.__dict__['relation']
            answer['voted_count'] = var.__dict__['voted_count']
            answer['comment_count'] = var.__dict__['comment_count']
            data.append(answer)
        response['count'] = len(data)
        response['data'] = data
        response = json.dumps(response, cls=DateEnconding)
        return response
    if question_id<=6905 and question_id>=5543:
        list = models.Answer_4.objects.filter(question_id=question_id)[:int(total_answer)]
        response = {}
        response['code'] = 0
        data = []
        for var in list:
            answer = {}
            answer['id'] = var.__dict__['id']
            answer['author'] = var.__dict__['author']
            answer['created_time'] = var.__dict__['created_time']
            answer['updated_time'] = var.__dict__['updated_time']
            answer['content'] = var.__dict__['content']
            answer['keywords'] = var.__dict__['keywords']
            answer['thanks_count'] = var.__dict__['thanks_count']
            answer['relation'] = var.__dict__['relation']
            answer['voted_count'] = var.__dict__['voted_count']
            answer['comment_count'] = var.__dict__['comment_count']
            data.append(answer)
        response['count'] = len(data)
        response['data'] = data
        response = json.dumps(response, cls=DateEnconding)
        return response
    if question_id<=7357 and question_id>=6906:
        list = models.Answer_5.objects.filter(question_id=question_id)[:int(total_answer)]
        response = {}
        response['code'] = 0
        data = []
        for var in list:
            answer = {}
            answer['id'] = var.__dict__['id']
            answer['author'] = var.__dict__['author']
            answer['created_time'] = var.__dict__['created_time']
            answer['updated_time'] = var.__dict__['updated_time']
            answer['content'] = var.__dict__['content']
            answer['keywords'] = var.__dict__['keywords']
            answer['thanks_count'] = var.__dict__['thanks_count']
            answer['relation'] = var.__dict__['relation']
            answer['voted_count'] = var.__dict__['voted_count']
            answer['comment_count'] = var.__dict__['comment_count']
            data.append(answer)
        response['count'] = len(data)
        response['data'] = data
        response = json.dumps(response, cls=DateEnconding)
        return response
    if question_id<=7415 and question_id>=7358:
        list = models.Answer_6.objects.filter(question_id=question_id)[:int(total_answer)]
        response = {}
        response['code'] = 0
        data = []
        for var in list:
            answer = {}
            answer['id'] = var.__dict__['id']
            answer['author'] = var.__dict__['author']
            answer['created_time'] = var.__dict__['created_time']
            answer['updated_time'] = var.__dict__['updated_time']
            answer['content'] = var.__dict__['content']
            answer['keywords'] = var.__dict__['keywords']
            answer['thanks_count'] = var.__dict__['thanks_count']
            answer['relation'] = var.__dict__['relation']
            answer['voted_count'] = var.__dict__['voted_count']
            answer['comment_count'] = var.__dict__['comment_count']
            data.append(answer)
        response['count'] = len(data)
        response['data'] = data
        response = json.dumps(response, cls=DateEnconding)
        return response

# 查询作者相关回答
def related_answer(author):
    question_id_list1 = models.Answer_1.objects.filter(author=author)
    question_id_list2 = models.Answer_2.objects.filter(author=author)
    question_id_list3 = models.Answer_3.objects.filter(author=author)
    question_id_list4 = models.Answer_4.objects.filter(author=author)
    question_id_list5 = models.Answer_5.objects.filter(author=author)
    question_id_list6 = models.Answer_6.objects.filter(author=author)
    list = []
    list.append(question_id_list1)
    list.append(question_id_list2)
    list.append(question_id_list3)
    list.append(question_id_list4)
    list.append(question_id_list5)
    list.append(question_id_list6)

    response = {}
    response['code'] = 0
    response['msg'] = ""
    data = []
    # 遍历每一个question_id
    for li in list:
        for var in li:
            related_answer = {}
            question_id = var.__dict__['question_id']
            related_answer['id'] = question_id
            related_answer['content'] = var.__dict__['content']
            related_answer['created_time'] = var.__dict__['created_time']
            related_answer['comment_count'] = var.__dict__['comment_count']
            related_answer['relation'] = var.__dict__['relation']
            related_answer['voted_count'] = var.__dict__['voted_count']
            related_answer['thanks_count'] = var.__dict__['thanks_count']
            if question_id >= 1 and question_id <= 1914:
                data1 = models.Question_1.objects.get(id=question_id)
                related_answer['question'] = data1.question_title
                related_answer['total_answer'] = data1.total_answer
            if question_id >= 1915 and question_id <= 2668:
                data1 = models.Question_2.objects.get(id=question_id)
                related_answer['question'] = data1.question_title
                related_answer['total_answer'] = data1.total_answer
            if question_id >= 2669 and question_id <= 5542:
                data1 = models.Question_3.objects.get(id=question_id)
                related_answer['question'] = data1.question_title
                related_answer['total_answer'] = data1.total_answer
            if question_id >= 5543 and question_id <= 6905:
                data1 = models.Question_4.objects.get(id=question_id)
                related_answer['question'] = data1.question_title
                related_answer['total_answer'] = data1.total_answer
            if question_id >= 6906 and question_id <= 7357:
                data1 = models.Question_5.objects.get(id=question_id)
                related_answer['question'] = data1.question_title
                related_answer['total_answer'] = data1.total_answer
            if question_id >= 7358 and question_id <= 7415:
                data1 = models.Question_6.objects.get(id=question_id)
                related_answer['question'] = data1.question_title
                related_answer['total_answer'] = data1.total_answer
            data.append(related_answer)
    print("相关回答"+str(data))
    response['data'] = data
    response = json.dumps(response,cls=DateEnconding)
    return  response

# 查找related_answer表
def related_search(keywords):
    list = models.answer_related_temp.objects.filter(question__icontains=keywords)
    response = {}
    response['code'] = 0
    response['msg'] = ""
    data = []
    for var in list:
        related_answer = {}
        related_answer['id'] = var.__dict__['id']
        related_answer['question'] = var.__dict__['question']
        related_answer['content'] = var.__dict__['content']
        related_answer['voted_up'] = var.__dict__['voted_count']
        related_answer['comment_count'] = var.__dict__['comment_count']
        related_answer['created_time'] = var.__dict__['created_time']
        related_answer['thanks_count'] = var.__dict__['thanks_count']
        related_answer['relation']  =var.__dict__['relation']
        data.append(related_answer)
    response['count'] = len(data)
    response['data'] = data
    response = json.dumps(response, cls=DateEnconding)
    return response

# 查找评论表
def get_comments(answer_id,comment_count):
    answer_id = int(answer_id)
    if(comment_count == '0'):
        response = {}
        data = []
        comments = {}
        comments['answer_id'] =[]
        comments['content'] = []
        comments['author'] = []
        comments['created_time'] = []
        comments['voted_count'] = []
        data.append(comments)
        response['data'] = data
        response['length'] = len(data)
        response = json.dumps(response, cls=DateEnconding)
        return response
    else:
        if answer_id >= 9 and answer_id <= 31871:
            # 获取满足条件的前comment_count个评论评论
            list = models.Comment_1.objects.filter(answer_id=answer_id)[:comment_count]
            response = {}
            data = []
            for var in list:
                comments = {}
                comments['answer_id'] = var.__dict__['answer_id']
                comments['content'] = var.__dict__['content']
                comments['author'] = var.__dict__['author']
                comments['created_time'] = var.__dict__['created_time']
                comments['voted_count'] = var.__dict__['voted_count']
                data.append(comments)
            response['data'] = data
            response['length'] = len(data)
            response = json.dumps(response, cls=DateEnconding)
            return response
        if answer_id >= 31783 and answer_id <= 43497:
            # 获取满足条件的前comment_count个评论评论
            list = models.Comment_2.objects.filter(answer_id=answer_id)[:comment_count]
            response = {}
            data = []
            for var in list:
                comments = {}
                comments['answer_id'] = var.__dict__['answer_id']
                comments['content'] = var.__dict__['content']
                comments['author'] = var.__dict__['author']
                comments['created_time'] = var.__dict__['created_time']
                comments['voted_count'] = var.__dict__['voted_count']
                data.append(comments)
            response['data'] = data
            response['length'] = len(data)
            response = json.dumps(response, cls=DateEnconding)
            return response
        if answer_id >= 43501 and answer_id <= 90463:
            # 获取满足条件的前comment_count个评论评论
            list = models.Comment_3.objects.filter(answer_id=answer_id)[:comment_count]
            response = {}
            data = []
            for var in list:
                comments = {}
                comments['answer_id'] = var.__dict__['answer_id']
                comments['content'] = var.__dict__['content']
                comments['author'] = var.__dict__['author']
                comments['created_time'] = var.__dict__['created_time']
                comments['voted_count'] = var.__dict__['voted_count']
                data.append(comments)
            response['data'] = data
            response['length'] = len(data)
            response = json.dumps(response, cls=DateEnconding)
            return response
        if answer_id >= 98879 and answer_id <= 114413:
            # 获取满足条件的前comment_count个评论评论
            list = models.Comment_4.objects.filter(answer_id=answer_id)[:comment_count]
            response = {}
            data = []
            for var in list:
                comments = {}
                comments['answer_id'] = var.__dict__['answer_id']
                comments['content'] = var.__dict__['content']
                comments['author'] = var.__dict__['author']
                comments['created_time'] = var.__dict__['created_time']
                comments['voted_count'] = var.__dict__['voted_count']
                data.append(comments)
            response['data'] = data
            response['length'] = len(data)
            response = json.dumps(response, cls=DateEnconding)
            return response
        if answer_id >= 114422 and answer_id <= 122124:
            # 获取满足条件的前comment_count个评论评论
            list = models.Comment_5.objects.filter(answer_id=answer_id)[:comment_count]
            response = {}
            data = []
            for var in list:
                comments = {}
                comments['answer_id'] = var.__dict__['answer_id']
                comments['content'] = var.__dict__['content']
                comments['author'] = var.__dict__['author']
                comments['created_time'] = var.__dict__['created_time']
                comments['voted_count'] = var.__dict__['voted_count']
                data.append(comments)
            response['data'] = data
            response['length'] = len(data)
            response = json.dumps(response, cls=DateEnconding)
            return response
        if answer_id >= 122148 and answer_id <= 123036:
            # 获取满足条件的前comment_count个评论评论
            list = models.Comment_6.objects.filter(answer_id=answer_id)[:comment_count]
            response = {}
            data = []
            for var in list:
                comments = {}
                comments['answer_id'] = var.__dict__['answer_id']
                comments['content'] = var.__dict__['content']
                comments['author'] = var.__dict__['author']
                comments['created_time'] = var.__dict__['created_time']
                comments['voted_count'] = var.__dict__['voted_count']
                data.append(comments)
            response['data'] = data
            response['length'] = len(data)
            response = json.dumps(response, cls=DateEnconding)
            return response




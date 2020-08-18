from django.http import HttpResponse
import json
from zhihu import mydb


# 查询接口函数
def question_search_1(request):
    print("查询问题")
    if request.method == 'POST':  # 当提交表单时
        response = {}
        # 判断是否传参
        if request.body:
            data = json.loads(request.body)
            if data:
                month = data.get('month')
                print("month="+month)
                response = mydb.question_search_1()
                return HttpResponse(response)
            else:
                return HttpResponse('输入错误')
        else:
            return HttpResponse('输入为空')
    else:
        return HttpResponse('方法错误')

# 查询接口函数
def question_search_2(request):
    print("查询问题")
    if request.method == 'POST':  # 当提交表单时
        response = {}
        # 判断是否传参
        if request.body:
            data = json.loads(request.body)
            if data:
                month = data.get('month')
                print("month="+month)
                response = mydb.question_search_2()
                return HttpResponse(response)
            else:
                return HttpResponse('输入错误')
        else:
            return HttpResponse('输入为空')
    else:
        return HttpResponse('方法错误')
# 查询接口函数
def question_search_3(request):
    print("查询问题")
    if request.method == 'POST':  # 当提交表单时
        response = {}
        # 判断是否传参
        if request.body:
            data = json.loads(request.body)
            if data:
                month = data.get('month')
                print("month="+month)
                response = mydb.question_search_3()
                return HttpResponse(response)
            else:
                return HttpResponse('输入错误')
        else:
            return HttpResponse('输入为空')
    else:
        return HttpResponse('方法错误')
# 查询接口函数
def question_search_4(request):
    print("查询问题")
    if request.method == 'POST':  # 当提交表单时
        response = {}
        # 判断是否传参
        if request.body:
            data = json.loads(request.body)
            if data:
                month = data.get('month')
                print("month="+month)
                response = mydb.question_search_4()
                return HttpResponse(response)
            else:
                return HttpResponse('输入错误')
        else:
            return HttpResponse('输入为空')
    else:
        return HttpResponse('方法错误')
# 查询接口函数
def question_search_5(request):
    print("查询问题")
    if request.method == 'POST':  # 当提交表单时
        response = {}
        # 判断是否传参
        if request.body:
            data = json.loads(request.body)
            if data:
                month = data.get('month')
                print("month="+month)
                response = mydb.question_search_5()
                return HttpResponse(response)
            else:
                return HttpResponse('输入错误')
        else:
            return HttpResponse('输入为空')
    else:
        return HttpResponse('方法错误')
# 查询接口函数
def question_search_6(request):
    print("查询问题")
    if request.method == 'POST':  # 当提交表单时
        response = {}
        # 判断是否传参
        if request.body:
            data = json.loads(request.body)
            if data:
                month = data.get('month')
                print("month="+month)
                response = mydb.question_search_6()
                return HttpResponse(response)
            else:
                return HttpResponse('输入错误')
        else:
            return HttpResponse('输入为空')
    else:
        return HttpResponse('方法错误')

# 点击questionlink进入answer界面
def answer_post(request):
    if request.method == 'POST':
        dic = {}
        # 判断是否传参
        if request.body:
            data = json.loads(request.body)
            if data:
                question_id = data.get('question_id')
                total_answer = data.get('total_answer')
                response = mydb.answer_post(question_id,total_answer)
                response1 = json.loads(response)
                response1['question_id'] = question_id
                print(response)
                return HttpResponse(response)
            else:
                return HttpResponse('输入错误')
        else:
            return HttpResponse('输入为空')
    else:
        return HttpResponse('方法错误')


#   查看作者相关回答
def related_answer(request):
    if request.body:
        data = json.loads(request.body)
        if data:
            # 获取作者
            author = data.get('author')
            response = mydb.related_answer(author)
            # mydb.insert_related_temp(response)
            return HttpResponse(response)
    else:
        return HttpResponse('方法错误')
# 获取评论数据
def get_comments(request):
    if request:
        data = json.loads(request.body.decode('utf-8'))
        if data:
            # 获取作者
            answer_id = data.get('answer_id')
            comment_count = data.get('comment_count')
            response = mydb.get_comments(answer_id, comment_count)
            response = json.loads(response)
            print(type(response))
            print(response)
            return HttpResponse(json.dumps(response),content_type='application/json')
    else:
        return HttpResponse('方法错误')




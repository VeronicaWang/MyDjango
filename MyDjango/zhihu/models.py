from django.db import models
# 模型类被定义在”应用/models.py”文件中。
# 模型类必须继承自Model类，位于包django.db.models中。
# Create your models here.
# 表的名字

class Question_1(models.Model):
    id = models.IntegerField(primary_key=True)
    question_title = models.TextField()
    follower_count = models.IntegerField()
    created_time = models.DateField()
    total_answer = models.IntegerField()
    detail = models.CharField(max_length=255)
    class Meta:
        db_table = 'zhihu_question'
class Question_2(models.Model):
    id = models.IntegerField(primary_key=True)
    question_title = models.TextField()
    follower_count = models.IntegerField()
    created_time = models.DateField()
    total_answer = models.IntegerField()
    detail = models.CharField(max_length=255)
    class Meta:
        db_table = 'zhihu_question_1'
class Question_3(models.Model):
    id = models.IntegerField(primary_key=True)
    question_title = models.TextField()
    follower_count = models.IntegerField()
    created_time = models.DateField()
    total_answer = models.IntegerField()
    detail = models.CharField(max_length=255)
    class Meta:
        db_table = 'zhihu_question_2'
class Question_4(models.Model):
    id = models.IntegerField(primary_key=True)
    question_title = models.TextField()
    follower_count = models.IntegerField()
    created_time = models.DateField()
    total_answer = models.IntegerField()
    detail = models.CharField(max_length=255)
    class Meta:
        db_table = 'zhihu_question_3'
class Question_5(models.Model):
    id = models.IntegerField(primary_key=True)
    question_title = models.TextField()
    follower_count = models.IntegerField()
    created_time = models.DateField()
    total_answer = models.IntegerField()
    detail = models.CharField(max_length=255)
    class Meta:
        db_table = 'zhihu_question_4'
class Question_6(models.Model):
    id = models.IntegerField(primary_key=True)
    question_title = models.TextField()
    follower_count = models.IntegerField()
    created_time = models.DateField()
    total_answer = models.IntegerField()
    detail = models.CharField(max_length=255)
    class Meta:
        db_table = 'zhihu_question_5'
class Answer_1(models.Model):
    id = models.IntegerField(primary_key=True)
    question_id =models.IntegerField()
    author = models.CharField(max_length=255)
    voted_count = models.IntegerField()
    comment_count = models.IntegerField()
    content = models.TextField()
    keywords = models.CharField(max_length=255)
    created_time = models.DateField()
    updated_time = models.DateField()
    relation = models.FloatField()
    thanks_count = models.IntegerField()
    class Meta:
        db_table='zhihu_answer'
class Answer_2(models.Model):
    id = models.IntegerField(primary_key=True)
    question_id =models.IntegerField()
    author = models.CharField(max_length=255)
    voted_count = models.IntegerField()
    comment_count = models.IntegerField()
    content = models.TextField()
    keywords = models.CharField(max_length=255)
    created_time = models.DateField()
    updated_time = models.DateField()
    relation = models.FloatField()
    thanks_count = models.IntegerField()
    class Meta:
        db_table='zhihu_answer_1'
class Answer_3(models.Model):
    id = models.IntegerField(primary_key=True)
    question_id =models.IntegerField()
    author = models.CharField(max_length=255)
    voted_count = models.IntegerField()
    comment_count = models.IntegerField()
    content = models.TextField()
    keywords = models.CharField(max_length=255)
    created_time = models.DateField()
    updated_time = models.DateField()
    relation = models.FloatField()
    thanks_count = models.IntegerField()
    class Meta:
        db_table='zhihu_answer_2'

class Answer_4(models.Model):
    id = models.IntegerField(primary_key=True)
    question_id =models.IntegerField()
    author = models.CharField(max_length=255)
    voted_count = models.IntegerField()
    comment_count = models.IntegerField()
    content = models.TextField()
    keywords = models.CharField(max_length=255)
    created_time = models.DateField()
    updated_time = models.DateField()
    relation = models.FloatField()
    thanks_count = models.IntegerField()
    class Meta:
        db_table='zhihu_answer_3'
class Answer_5(models.Model):
    id = models.IntegerField(primary_key=True)
    question_id =models.IntegerField()
    author = models.CharField(max_length=255)
    voted_count = models.IntegerField()
    comment_count = models.IntegerField()
    content = models.TextField()
    keywords = models.CharField(max_length=255)
    created_time = models.DateField()
    updated_time = models.DateField()
    relation = models.FloatField()
    thanks_count = models.IntegerField()
    class Meta:
        db_table='zhihu_answer_4'
class Answer_6(models.Model):
    id = models.IntegerField(primary_key=True)
    question_id =models.IntegerField()
    author = models.CharField(max_length=255)
    voted_count = models.IntegerField()
    comment_count = models.IntegerField()
    content = models.TextField()
    keywords = models.CharField(max_length=255)
    created_time = models.DateField()
    updated_time = models.DateField()
    relation = models.FloatField()
    thanks_count = models.IntegerField()
    class Meta:
        db_table='zhihu_answer_5'


#  评论表
class Comment_1(models.Model):
    id = models.IntegerField(primary_key=True)
    answer_id = models.IntegerField()
    content = models.TextField()
    author = models.CharField(max_length=255)
    created_time = models.DateField()
    voted_count = models.IntegerField()
    class Meta:
        db_table = 'zhihu_comment'
class Comment_2(models.Model):
    id = models.IntegerField(primary_key=True)
    answer_id = models.IntegerField()
    content = models.TextField()
    author = models.CharField(max_length=255)
    created_time = models.DateField()
    voted_count = models.IntegerField()
    class Meta:
        db_table = 'zhihu_comment_1'
class Comment_3(models.Model):
    id = models.IntegerField(primary_key=True)
    answer_id = models.IntegerField()
    content = models.TextField()
    author = models.CharField(max_length=255)
    created_time = models.DateField()
    voted_count = models.IntegerField()
    class Meta:
        db_table = 'zhihu_comment_2'
class Comment_4(models.Model):
    id = models.IntegerField(primary_key=True)
    answer_id = models.IntegerField()
    content = models.TextField()
    author = models.CharField(max_length=255)
    created_time = models.DateField()
    voted_count = models.IntegerField()
    class Meta:
        db_table = 'zhihu_comment_3'
class Comment_5(models.Model):
    id = models.IntegerField(primary_key=True)
    answer_id = models.IntegerField()
    content = models.TextField()
    author = models.CharField(max_length=255)
    created_time = models.DateField()
    voted_count = models.IntegerField()
    class Meta:
        db_table = 'zhihu_comment_4'

class Comment_6(models.Model):
    id = models.IntegerField(primary_key=True)
    answer_id = models.IntegerField()
    content = models.TextField()
    author = models.CharField(max_length=255)
    created_time = models.DateField()
    voted_count = models.IntegerField()
    class Meta:
        db_table = 'zhihu_comment_5'
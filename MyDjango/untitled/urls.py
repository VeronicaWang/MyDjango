"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_connection import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from zhihu import views

urlpatterns = [
    path('question_search_1/', views.question_search_1),
    path('question_search_2/', views.question_search_2),
    path('question_search_3/', views.question_search_3),
    path('question_search_4/', views.question_search_4),
    path('question_search_5/', views.question_search_5),
    path('question_search_6/', views.question_search_6),
    path('answer_post/', views.answer_post),
    path('related_answer/', views.related_answer),
    path('get_comments/', views.get_comments),

]

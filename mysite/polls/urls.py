from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # exercise: trying out to add another view using the shortcut render
    path('index2/', views.index2, name='index2'),
    # added the word 'specifics'
    path('specifics/<int:question_id>/', views.detail, name='detail'),
]
from django.urls import path
from . import views

app_name = 'to_do'

urlpatterns = [
    path('board-create/', views.BoardCreateApi.as_view()),
    path('board-list/', views.BoardListApi.as_view()),
]
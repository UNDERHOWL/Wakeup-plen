#システムにアクセスがあればトップページに飛ばす」といった設定
#app_config/views.pyは全体を大まかにコントロールする

from django.urls import path
from . import views
from app_config import views as userview

app_name = 'app_folder'
urlpatterns = [
    path('top_page/', views.top_page, name='top_page'),

    #path('user_detail/<int:pk>/', userview.UserDetail.as_view(), name='user_detail'),
   
]

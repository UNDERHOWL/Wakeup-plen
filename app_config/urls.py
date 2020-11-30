"""app_config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path #10/16追加
from app_folder import views as default_views

# URLの全体設計

app_name = 'app_folder'

urlpatterns = [
    # 今回作成するアプリ「app_folder」にアクセスするURL
    path('app_folder/', include('app_folder.urls')),
    # 何もURLを指定しない場合（app_config/views.pyで、自動的に「app_folder」にアクセスするよう設定済み）
    path('', views.index, name='index'),
    # 管理サイトにアクセスするURL
    path('admin/', admin.site.urls),
    #サインアップ画面にアクセスするURL 10/16追加
    path('default-signup/', default_views.signup, name='default_signup'),

    path('login/', views.Login.as_view(), name='login'), #10/19追加
    
    path('logout/', views.Logout.as_view(), name='logout'),

    path('post', views.PostandBoard.as_view(), name='PostandBoard'), #11/2

    path('post-list', views.post_list.as_view(), name='post_list'),

    path('mypage/<int:pk>/', views.MyPage.as_view(), name='mypage'),
    
    path('top_page/', views.Top_Page.as_view(), name='top_page'),

    path('obniz/', views.Obniz.as_view(), name='obniz'),
]

# メディアファイル公開用のURL設定
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
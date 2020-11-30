from django.shortcuts import render, redirect, reverse, get_object_or_404  
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #10/23追加
from django.contrib.auth.views import (
    LoginView, LogoutView
)
from django.views import generic
from app_folder.forms import LoginForm
from app_folder.models import Post
from app_folder.forms import PostForm
from django.views.generic.edit import ModelFormMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import HttpResponseBadRequest
from django.views.generic import CreateView, FormView, DetailView, ListView, TemplateView

User = get_user_model()

class index(View):
    def get(self, request, *args, **kwargs):
        return redirect(reverse('app_folder:top_page'))
index = index.as_view()


class Top_Page(TemplateView):
    template_name = 'app_folder/top_page.html'

class default_signup(View): #10月16日追加
    def get(self, request, *args, **kwargs):
        return redirect(reverse('app_folder:default_signup'))
default_signup = default_signup.as_view()

class Login(LoginView): #10/23追加
    """ログインページ"""
    form_class = LoginForm
    template_name = 'app_folder/login.html'


class Logout(LogoutView):
    """ログアウトページ"""
    template_name = 'app_folder/mypage.html'

class PostandBoard(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'app_folder/board.html'


class post_list(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-date')


class MyPage(DetailView):
    template_name = 'app_folder/mypage.html'
    model = User
    context_object_name = 'mypage'
   
    
class Obniz(TemplateView):
    template_name = "app_folder/obniz.html"





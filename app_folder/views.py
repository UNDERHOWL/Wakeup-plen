#トップページにアクセスされたらoo.htmlを表示する
#app_folder/views.pyは個々の機能をコントロールする

from django.shortcuts import render  
from django.views import View  
from .models import SampleDB
from django.contrib.auth import login, authenticate #10/16追加
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


class SampleView(View):  
    def get(self, request, *args, **kwargs):  
        return render(request, 'app_folder/page01.html')

    def post(self, request, *args, **kwargs):  
        input_data = request.POST['input_data']
        result = SampleDB.objects.filter(sample1=input_data)
        result_sample1 = result[0].sample1
        result_sample2 = result[0].sample2
        context={'result_sample1':result_sample1, 'result_sample2':result_sample2}
        return render(request, 'app_folder/page02.html', context=context,)

top_page = SampleView.as_view()

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/top_page')
    else:
        form = UserCreationForm()
    return render(request, 'app_folder/signup.html', {'form': form})


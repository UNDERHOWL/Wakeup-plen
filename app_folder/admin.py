from django.contrib import admin
from .models import SampleDB # models.pyで指定したクラス名
from .models import Post

admin.site.register(SampleDB) # models.pyで指定したクラス名

class PostAdmin(admin.ModelAdmin):
    search_fields = ['text']





admin.site.register(Post, PostAdmin)
from django.db import models
from django.utils import timezone #10/30
from django.urls import reverse
from django.shortcuts import render, redirect, reverse



class SampleDB(models.Model):
    class Meta:
        db_table = 'sample_table' # DB内で使用するテーブル名
        verbose_name_plural = 'sample_table' # Admionサイトで表示するテーブル名
    sample1 = models.IntegerField('sample1', null=True, blank=True) # 数値を格納
    sample2 = models.CharField('sample2', max_length=255, null=True, blank=True) # 文字列を格納

class Post(models.Model):
    name = models.CharField('名前', max_length=20) #11/2
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)
        
        
    def get_absolute_url(self):
        return reverse('post_list')





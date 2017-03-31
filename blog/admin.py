#coding:utf-8
from django.contrib import admin
from blog.models import Post
#from django_markdown.admin import MarkdownModelAdmin
from django import forms

#from pagedown.widgets import AdminPagedownWidget

admin.site.register(Post)



# Register your models here.
#class ArticleForm(forms.ModelForm):
#    content = forms.CharField(widget=AdminPagedownWidget())
#    class Meta:
#        model = Post 
#        fields = '__all__'
#class ArticleAdmin(admin.ModelAdmin):
#    form = ArticleForm

#admin.site.register(Post,ArticleAdmin)








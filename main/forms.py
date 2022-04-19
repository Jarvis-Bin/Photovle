from cProfile import label
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

# 유저 생성 form
class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    phone = forms.CharField(label='전화번호')
    class Meta:
        model = User
        fields = ('name', 'username', 'password1', 'password2', 'email', 'phone')

# 게시판 글쓰기 form
class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'content', 'upload_files']

# 게시판 댓글 form
class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['comment']
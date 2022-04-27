from pyexpat import model
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import info

# CRUD 페이지.
# 메인
class mainView(ListView):
    model = info
    template_name_suffix = '_main';

# 뷰페이지 데이터 조회
class infoListView(ListView):
    model = info;
    template_name_suffix = '_list';

# 데이터 생성
class infoListCreateView(CreateView):
    model = info;
    fields = ['site_name'];
    success_url = reverse_lazy('main');
    template_name_suffix = '_create';
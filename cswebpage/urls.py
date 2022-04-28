from django.urls import path
from .views import sqlStudySiteMapping ,infoListCreateView, infoListView, mainView

urlpatterns = [
    # as_view() : 클래스형 뷰를 내부적으로 함수형 뷰로 처리
    # name : 결과 페이지로 보여 줄 템플릿 파일에서 해당 URL을 호출할 때 쓰는 별칭
    path('', mainView.as_view(),name="main"),
    path('list/', infoListView.as_view(), name='list'),  # http://127.0.0.1/cswebpage/
    path('add/', infoListCreateView.as_view(), name='add'),

    # study site mapping
    path('study/sql/',sqlStudySiteMapping.as_view(), name='sql'),
]
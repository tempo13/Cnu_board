from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.blog_data, name='blog_data'),
    url(r'^$', views.post_list, name='post_list'),

    #11/2 url의 쓰인 순서에 따라 post_list.html에 출력되는게 다름
]
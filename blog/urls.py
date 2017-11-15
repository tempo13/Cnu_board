from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [

    url(r'^market/$', views.parse_data, name='parse_data'),
    url(r'^$', views.blog_data, name='blog_data'),
    url(r'^post/$', views.post_list, name='post_list'),
    url(r'^board/$', views.board_data, name='board_data'),

    #11/2 url의 쓰인 순서에 따라 post_list.html에 출력되는게 다름

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

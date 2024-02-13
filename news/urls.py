from django.urls import path
from . import views
app_name = 'news'

urlpatterns = [
    path('', views.home, name='news'),
    path('news/<pk>', views.news, name='select-news')
]
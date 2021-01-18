from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('post/<str:slug>/', post_detail, name='post_detail'),
    path('tag/<str:slug>/', tags, name='tags')
]
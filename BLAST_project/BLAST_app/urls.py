from django.urls import path
from . import views, forms

urlpatterns = [
    path('', views.home, name='Home_page'),
    path('result/', views.result, name='Result_page')
]

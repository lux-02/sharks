from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('blog/', views.blog_view),
    path('submit_registration/', views.submit_registration, name='submit_registration'),
    path('submit_signin/', views.submit_signin, name='submit_signin'),
    path('signout/', views.signout, name='signout'),
    path('post_reply/', views.post_reply, name='post_reply'),
]



from django.urls import path
from . import views

urlpatterns = [
    path('predict/', views.predict_text, name='predict_text'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('',views.index_view,name='index'),
]

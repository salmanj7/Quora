from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('ask/', views.ask_question_view, name='ask'),
    path('question/<int:pk>/', views.question_detail_view, name='question_detail'),
    path('answer/<int:pk>/like/', views.like_answer_view, name='like_answer'),
]

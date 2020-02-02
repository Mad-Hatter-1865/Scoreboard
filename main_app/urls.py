from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/',views.ScoreCreate.as_view(), name='scores_create'),
    path('<int:pk>/delete/', views.ScoreDelete.as_view(), name='scores_delete'),
]
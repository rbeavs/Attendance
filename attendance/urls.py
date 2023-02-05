from django.urls import path
from . import views

app_name = 'attendance'
urlpatterns = [
    path('', views.index, name='index'),
    path('completed', views.completed_detail, name='completed'),
    path('rankings', views.rankings_view, name='rankings'),
    path('winner', views.winner, name='winner'),
]

from django.urls import path
from history import views

app_name = 'history'

urlpatterns = [
    path('activity/', views.trials, name='trials'),
]

#THIS IS A CREATED FILE AFTER UPDATING VIEWS

from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_obituary, name='submit_obituary'),
    path('', views.view_obituaries, name='view_obituaries'),
]

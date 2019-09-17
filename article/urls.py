from django.urls import path

from article import views
from .views import *

urlpatterns = [
    path('ss/',views.ss),
]
from django.urls import path
from . import views

urlpatterns=[
        path('signup',views.teacher_signup)

]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Feedback.as_view()),
    path('thanks', views.ThankYou.as_view()),
]

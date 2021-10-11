from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view()),
    path('thanks', views.ThankYou.as_view()),
    path('reviews', views.ReviewList.as_view()),
    path('reviews/<int:id>', views.ReviewDetails.as_view()),
]

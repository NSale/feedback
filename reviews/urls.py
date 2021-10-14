from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view()),
    path('thanks', views.ThankYou.as_view()),
    path('reviews', views.ReviewList.as_view()),
    path('reviews/favorite', views.AddFavorite.as_view()),
    path('reviews/<int:pk>', views.ReviewDetails.as_view()),
]

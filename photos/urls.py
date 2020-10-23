from django.urls import path
from . import views

urlpatterns = [
    path('photos/', views.PhotoListView.as_view()),
    path('photo/<int:pk>/', views.PhotoDetailView.as_view()),
    path('comment/', views.CommentCreateView.as_view()),
]
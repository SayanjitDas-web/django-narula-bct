from django.urls import path
from .views import HomeView, PostDetailView, CreatePostView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('create/', CreatePostView.as_view(), name='create'),
    path('delete/<int:pk>/', DeletePostView.as_view(), name='delete'),
]
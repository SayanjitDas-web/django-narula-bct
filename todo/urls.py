from django.urls import path
from .views import PostCreateView, PostDeleteView, PostListView, PostUpdateView

urlpatterns = [
    path("",PostListView.as_view(),name="post_list"),
    path("create/",PostCreateView.as_view(),name="post_create"),
    path("update/<int:pk>/",PostUpdateView.as_view(),name="post_update"),
    path("delete/<int:pk>/",PostDeleteView.as_view(),name="post_delete"),
]
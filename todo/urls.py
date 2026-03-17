from django.urls import path
from .views import PostCreateView, PostDeleteView, PostListView, PostUpdateView, SignUpView, DocumentUploadView, success_view

urlpatterns = [
    path("",PostListView.as_view(),name="post_list"),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('upload/', DocumentUploadView.as_view(), name='upload'),
    path('success/', success_view, name='success'),
    path("create/",PostCreateView.as_view(),name="post_create"),
    path("update/<int:pk>/",PostUpdateView.as_view(),name="post_update"),
    path("delete/<int:pk>/",PostDeleteView.as_view(),name="post_delete"),
]
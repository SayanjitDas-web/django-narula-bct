from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Post
from django.urls import reverse_lazy

class PostCreateView(CreateView):
    model = Post
    fields = ["title","content"]
    template_name = "post_form.html"
    success_url = reverse_lazy("post_list")

class PostUpdateView(UpdateView):
    model = Post
    fields = ["title","content"]
    template_name = "post_form.html"
    success_url = reverse_lazy("post_list")

class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

class PostListView(ListView):
    model = Post
    template_name = "post_list.html"
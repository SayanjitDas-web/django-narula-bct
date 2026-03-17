from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ["title","content"]
    template_name = "post_form.html"
    success_url = reverse_lazy("post_list")

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    fields = ["title","content"]
    template_name = "post_form.html"
    success_url = reverse_lazy("post_list")

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

class PostListView(ListView):
    model = Post
    template_name = "post_list.html"

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
from django.shortcuts import  render
from django.views.generic import TemplateView, ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from blogfinal.models import Post

def index(request):
    return render(request,"blogfinal/index.html", {})

class PostList(ListView):
    model = Post

class Postcrear(CreateView):
    model = Post
    success_url =reverse_lazy("listar") #"/blogfinal/listar"
    fields = '__all__'

class Postborrar(DeleteView):
    model = Post
    success_url = "/blogfinal/listar"
    fields = '__all__'
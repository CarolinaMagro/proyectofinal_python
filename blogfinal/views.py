from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import  render
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from blogfinal.forms import UsuarioForm
from blogfinal.models import Post

@login_required
def index(request):
    return render(request,"blogfinal/index.html", {})

class PostList(ListView):
    model = Post

class Postcrear(LoginRequiredMixin , CreateView):
    model = Post
    success_url =reverse_lazy("listar") #"/blogfinal/listar"
    fields = '__all__'

class PostBorrar(LoginRequiredMixin , DeleteView):
    model = Post
    success_url = reverse_lazy('borrar')

class PostActualizar(LoginRequiredMixin , UpdateView):
    model = Post
    success_url = reverse_lazy("listar") #"/blogfinal/listar"
    fields = '__all__'
class PostDetalle(DetailView):
    model = Post
    success_url = reverse_lazy("detalle")

class UserSingUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url= reverse_lazy('listar')

class UserLogin(LoginView):
    next_page = reverse_lazy('listar')

class UserLogOut(LogoutView):
    next_page = reverse_lazy('listar')
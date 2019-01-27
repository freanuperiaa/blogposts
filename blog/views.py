from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    object_list = Post.objects.all()
    context = {
        'items' : object_list,
    }
    return render(request, 'home.html', context)

class BlogDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'post_edit.html'

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
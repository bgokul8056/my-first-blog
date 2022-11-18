from django.utils import timezone
from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User
# Create your views here.

def post_list(request):
    me = User.objects.get(username='gokul')
    posts = Post.objects.filter(author = me).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
from django.shortcuts import render
from .models import Post, Comment

# Create your views here.

def post_list(request):

    filtro = request.GET.get('filtro')

    if filtro:
        posts = Post.objects.filter(title__icontains=filtro)
    else:
        posts = Post.objects.all()

    return render(
        request,
        'blog/post_list.html',
        {'posts':posts}
    )

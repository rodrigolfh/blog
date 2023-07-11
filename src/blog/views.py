from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm
from django.views.generic import ListView

# Create your views here.

# def post_list(request):

#     filtro = request.GET.get('filtro')

#     if filtro:
#         posts = Post.objects.filter(title__icontains=filtro)
#     else:
#         posts = Post.objects.all()

#     return render(
#         request,
#         'blog/post_list.html',
#         {'posts':posts}
#     )

def crear_posteo(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            author = form.cleaned_data["author"]
            tzone = form.cleaned_data["tzone"]
            post = Post.objects.create(
                title=title,
                content=content,
                author=author,
                tzone=tzone
            )
            return redirect("post_list")
        else:
            return render(request, 'blog/crear_posteo.html', {'form':form})
    
    return render(request, 'blog/crear_posteo.html', {'form':form})

def modificar_posteo(request, id):
    post = Post.objects.get(pk=id)
    form = PostForm(instance=post)
    if request.method =="POST":
        form = PostForm(request.POST, instance=post)
        form.save()
        return redirect('post_list')
    else:
        return render(request, 'blog/modificar_posteo.html', {'form':form})
    
def eliminar_posteo(request, id):
    post = Post.objects.get(pk=id)

    if request.method == "POST":
        post.delete()
        return redirect('post_list')


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'post'

    def get_queryset(self):
        queryset = super().get_queryset()
        filtro = self.request.GET.get('filtro')

        if filtro:
            queryset = queryset.filter(title__icontains=filtro)

        return queryset
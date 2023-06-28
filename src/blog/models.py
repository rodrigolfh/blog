from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    TZ = [
        ("EU", "EUROPE"),
        ("AS", "ASIA"),
        ("US", "UNITED STATES"),
    ]
    title = models.CharField(verbose_name="Titulo del Posteo", max_length=100)
    content = models.TextField(verbose_name="Texto del Posteo", null=True, blank=True, default="Texto default")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor del Posteo")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Horario del posteo")
    tzone = models.CharField(choices=TZ, verbose_name="Zona horaria")

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.author.username} en {self.post.title}"
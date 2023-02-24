from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    caption=models.CharField(max_length=255)

    def __str__(self):
        return self.caption



class Author(models.Model):
    first_name=models.CharField(max_length=255) 
    last_name=models.CharField(max_length=255)   
    email=models.EmailField()
    user=models.OneToOneField(User ,on_delete=models.CASCADE ,null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Post(models.Model):
    title=models.CharField(max_length=255)
    excerpt=models.CharField(max_length=255)
    date=models.DateTimeField(auto_now=True)
    slug=models.SlugField(unique=True ,db_index=True)
    image=models.ImageField(upload_to='posts',null=True)
    image_name=models.CharField(max_length=255)
    content=models.TextField(validators=[MinLengthValidator(10)])
    author=models.ForeignKey(Author , on_delete=models.SET_NULL ,null=True,related_name='posts')
    tags=models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(models.Model):
    username=models.CharField(max_length=255)
    email=models.EmailField()
    text=models.TextField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE ,related_name='comments')      
    is_approved=models.BooleanField(default=True)



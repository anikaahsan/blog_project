from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption=models.CharField(max_length=255)

    def __str__(self):
        return self.caption



class Author(models.Model):
    first_name=models.CharField(max_length=255) 
    last_name=models.CharField(max_length=255)   
    email=models.EmailField()

    def __str__(self):
        return self.first_name


class Post(models.Model):
    title=models.CharField(max_length=255)
    excerpt=models.CharField(max_length=255)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(unique=True ,db_index=True)
    #image=models.ImageField()
    image_name=models.CharField(max_length=255)
    content=models.TextField(validators=[MinLengthValidator(10)])
    author=models.ForeignKey(Author , on_delete=models.SET_NULL ,null=True,related_name='posts')
    tags=models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
   


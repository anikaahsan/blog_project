from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    title=models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title=models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    title=models.CharField(max_length=255)
    excerpt=models.CharField(max_length=255,null=True,blank=True)
    date=models.DateTimeField(auto_now=True,null=True,blank=True)
    slug=models.SlugField( null=True, blank=True)
    image=models.ImageField(upload_to='posts',null=True)
    content=models.TextField()
    author=models.ForeignKey(User , on_delete=models.SET_NULL ,null=True,related_name='posts')
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
    tags=models.ManyToManyField(Tag,related_name='posts')
    likes=models.ManyToManyField(User,related_name='post_liked')
    month_year=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.title
    
    def slugify(self):
        slug=slugify(self.title)
        return slug


class Comment(models.Model):
    username=models.CharField(max_length=255)
    email=models.EmailField(null=True,blank=True)
    text=models.TextField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE ,related_name='comments')      
    is_approved=models.BooleanField(default=True)
    









# validators=[MinLengthValidator(10)]

# Create your models here.




# class Author(models.Model):
#     first_name=models.CharField(max_length=255) 
#     last_name=models.CharField(max_length=255)   
#     email=models.EmailField()
#     user=models.OneToOneField(User ,on_delete=models.CASCADE ,null=True)

#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"

#     def __str__(self):
#         return self.full_name()

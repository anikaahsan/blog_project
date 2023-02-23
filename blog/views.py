from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Author,Tag
from .forms import CommentForm

# Create your views here.
def starting_page(request):
    queryset=Post.objects.all().order_by("date")[ :3]

    return render(request,'blog/index.html' ,{'post':queryset})


def posts(request):
    queryset=Post.objects.all()
    return render(request,'blog/all-posts.html' ,{'post':queryset})


def post_detail(request,slug):
    if request.method=='POST':
        commentform=CommentForm(request.POST)
        if commentform.is_valid():
            commentform.save()
            print("saved")
        else:
            return HttpResponse("error")    
        return render(request, 'blog/post-detail.html',{'form':commentform})

    else:    
        post =Post.objects.get(slug=slug)
        commentform=CommentForm()

        context=dict(post=post ,
        form=commentform)

        return render(request, 'blog/post-detail.html' ,context)

    
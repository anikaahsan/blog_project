from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Post,   Comment
from .forms import CommentForm,UserForm,WritePostForm
from django.template.defaultfilters import slugify
from django.contrib import messages

# Create your views here.
def starting_page(request):
    queryset=Post.objects.all().order_by('-date')[ :3]

    return render(request,'blog/index.html' ,{'post':queryset})


def posts(request):
    queryset=Post.objects.all()
    return render(request,'blog/all-posts.html' ,{'post':queryset})


def post_detail(request,slug):
    if request.method=='POST':
        commentform=CommentForm(request.POST)
        if commentform.is_valid():
            comment=commentform.save(commit=False)
            comment.post=Post.objects.get(slug=slug)
            comment.save()
            print("saved")
            return HttpResponseRedirect(reverse('post-detail-page', args=[slug]))
        else:
            return HttpResponse("error")    
        return render(request, 'blog/post-detail.html',{'form':commentform})

    else:    
        post =Post.objects.get(slug=slug)
        commentform=CommentForm()
        comment=Comment.objects.filter(post=post).order_by('-pk')
        context=dict(post=post ,
        form=commentform,
        comments=comment)

        return render(request, 'blog/post-detail.html' ,context)

def signup_function(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'signup successful')
            return redirect('login')
        else:
            
            return redirect('signup')


    else:
        signupform=UserForm()
        return render(request ,'blog/signupform.html',{'form':signupform})      





def approve(request ,id ):
    commentobject=Comment.objects.get(pk=id)
    commentobject.is_approved=False 


def comment_delete(request,id):
    commentobject=Comment.objects.get(pk=id)
    commentobject.delete()    


def write_post(request):
    if request.method=='POST':
        postform=WritePostForm(request.POST, request.FILES)
        print("form")
        print(postform.__dict__)
        if postform.is_valid():
            postform.save(commit=True)
            return redirect('posts-page')
        else:
            print(postform.errors)
            print('not saved') 
            return redirect('write-post')  




    else:    
        postform=WritePostForm()
        context=dict(form=postform)
        return render(request,'blog/writepost.html',context)    
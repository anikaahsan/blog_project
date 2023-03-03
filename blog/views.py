from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post,   Comment
from .forms import CommentForm,UserForm,WritePostForm



def starting_page(request):
    queryset=Post.objects.all().order_by('-date')[ :3]

    return render(request,'blog/index.html' ,{'post':queryset})


def posts(request):
    queryset=Post.objects.all()
    return render(request,'blog/all-posts.html' ,{'post':queryset})


def post_detail(request,pk):
    if request.method=='POST':
        commentform=CommentForm(request.POST)
        
        print(commentform.__dict__)

        if commentform.is_valid():
            comment=commentform.save(commit=False)
            comment.post=Post.objects.get(pk=pk)
            if request.user.is_authenticated:
               comment.email=request.user.email
            print(comment.__dict__)
            comment.save()
            print("saved")
            return HttpResponseRedirect(reverse('post-detail-page', args=[pk]))
        else:
            print(commentform.errors)
            return HttpResponse("error")    
        

    else:    
        post =Post.objects.get(pk=pk)
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
            print(form.errors)
            context=dict(errors=form.errors,
                         form=form)
            return render(request ,'blog/signupform.html' ,context)


    else:
        signupform=UserForm()
        return render(request ,'blog/signupform.html',{'form':signupform})      




@login_required
def approve(request ,id ):
    commentobject=Comment.objects.get(pk=id)
    commentobject.is_approved=False 
    return redirect('posts-page')
    # return HttpResponseRedirect(reverse('post-detail-page', args=[id]))



@login_required
def comment_delete(request,id):
    commentobject=Comment.objects.get(pk=id)
    commentobject.delete()
    return redirect('posts-page')
    # return HttpResponseRedirect(reverse('post-detail-page', args=[id])) 



@login_required
def write_post(request):
    if request.method=='POST':
        postform=WritePostForm(request.POST, request.FILES)
      
        print(postform.__dict__)

        if postform.is_valid():
            form=postform.save(commit=False)
            form.author=request.user
            print( form.__dict__)

            print(form.author)

            form.save()
            return redirect('posts-page')
        
        else:
            print(postform.errors)
            print('not saved') 
            return redirect('write-post')  




    else:    
        postform=WritePostForm()
        context=dict(form=postform)
        return render(request,'blog/writepost.html',context)    
    





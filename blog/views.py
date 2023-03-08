from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models.functions import ExtractMonth
from django.http import Http404
from .models import Post,   Comment,Category
from .forms import CommentForm,UserForm,WritePostForm
import calendar


def error_404_view(request,exception):
    return render(request,'blog/404.html')

def starting_page(request):
        queryset=Post.objects.all().order_by('-date')[ :3]

        categories=Category.objects.all()
        postmonth_list=[]
        postmonth_uniquelist=[]
        posts=Post.objects.all().annotate(post_month=ExtractMonth('date'))

        for post in posts:
            post_months=calendar.month_name[post.post_month]
            postmonth_list.append(post_months)
        
        for x in postmonth_list:
                if x not in postmonth_uniquelist:
                     postmonth_uniquelist.append(x)

        print(postmonth_uniquelist)    




        context=dict(categories=categories,
                     post=queryset,
                     months=postmonth_uniquelist) 

        return render(request,'blog/index.html' ,context)

  
        

def posts(request):
    queryset=Post.objects.all()
    paginator=Paginator(queryset,3) 
    page_number=request.GET.get('page')
    subqueryset=paginator.get_page(page_number)
    totalpages=paginator.num_pages

    totalpage=[ n+1 for n in range(totalpages)]
    
    context=dict(totalpages=totalpage,
                 post=subqueryset)

    return render(request,'blog/all-posts.html' ,context)



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
    




@login_required
def author_all_posts(request , pk):
    try:
        post=Post.objects.get(pk=pk)
        author=post.author
        queryset=Post.objects.filter(author=author)
    except Exception:
                return render(request,'blog/404.html')
    
    context=dict(queryset=queryset,
                    author=author)

    return render(request,'blog/author_all_post_beautiful.html' , context)
   

  
def post_detail(request,pk):   
        if request.method=='POST':
            commentform=CommentForm(request.POST)
            
            print(commentform.__dict__)

            if commentform.is_valid():
                comment=commentform.save(commit=False)
                try:
                   comment.post=Post.objects.get(pk=pk)
                except Exception:
                  return render(request,'blog/404.html')
                
                if request.user.is_authenticated:
                   comment.email=request.user.email

                print(comment.__dict__)
                comment.save()
                return HttpResponseRedirect(reverse('beautiful', args=[pk]))
            
            else:
                print(commentform.errors)
                return HttpResponse("error")    
            

        else:
            try:         
                post =Post.objects.get(pk=pk)
                related_post=Post.objects.filter(category=post.category)  
                commentform=CommentForm()
                comment=Comment.objects.filter(post=post).order_by('-pk')
            
            except Exception:
                return render(request,'blog/404.html')
            context=dict(
                        post=post ,
                        form=commentform,
                        comments=comment,
                        related_post=related_post
                        )

            return render(request, 'blog/post_detail_beautiful.html' ,context)
    


def search(request):
    if request.method=='POST':
        search=request.POST['search']
        queryset=Post.objects.filter(category__title__contains=search)
     
        queryset_2=Post.objects.filter(tags__title__contains=search)
       
        queryset_3=Post.objects.filter(title__contains=search)     

        context=dict(search=search,
                     posts=queryset,
                     posts_2=queryset_2,
                     posts_3=queryset_3
                     )
        
        return render(request,'blog/search.html',context)

    else:
        return render(request,'blog/search.html')




def category(request,category ):
   category=category
   posts=Post.objects.filter(category__title=category)

   context=dict(posts=posts,
                category=category)
   return render(request , 'blog/categorypost.html',context)


def month_post(request ,month ):
     posts=Post.objects.filter()
     



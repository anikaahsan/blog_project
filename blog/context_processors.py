from django.db.models.functions import ExtractMonth
from django.db.models import F
from .models import Category,Post
import calendar





def category(request ):
        categories=Category.objects.all()
        postmonth_list=[]
        postmonth_uniquelist=[]
        posts=Post.objects.all().annotate(post_month=ExtractMonth('date'))
        

        for post in posts:
            post_months=calendar.month_name[post.post_month]
            postmonth_list.append(f'{post_months}{post.date.year}')
        
        for x in postmonth_list:
                if x not in postmonth_uniquelist:
                     postmonth_uniquelist.append(x)

        print(postmonth_uniquelist) 
        
        context=dict(categories=categories,
                      months_years=postmonth_uniquelist,
                      )
        
        return context


# def archive(request,month_years):
#         posts=Post.objects.annotate(month=ExtractMonth('date') ,year=F('date'))
    
#         for post in posts:
#             post.month=calendar.month_name[post.month]
#             post.year=post.date.year
#             post.month_year=f'{post.month}{post.year}'
            
#             print(f'{post.month}{post.year}')
            
#         for post in posts:
#             print(post.month_year)
#         #  posts_all=Post.objects.filter(month_year=month_years)

#         queryset=[]
#         for post in posts:
#             if post.month_year==month_years:
#                 queryset.append(post)
            
#         context=dict(posts=queryset,
#                   month_year=month_years) 
#         return context
        
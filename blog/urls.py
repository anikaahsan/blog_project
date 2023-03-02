from django.urls import path
from django.contrib.auth import views as auth_view
from blog import views

urlpatterns=[
             path('', views.starting_page  ,name='starting-page'),
             path('posts/', views.posts ,name='posts-page'),
             path('posts/<pk>/', views.post_detail ,name='post-detail-page')  ,
             path('signup/' ,views.signup_function ,name='signup'),
             path('login/', auth_view.LoginView.as_view(template_name='blog/loginform.html') ,name='login'),
             path('logout',auth_view.LogoutView.as_view(template_name='blog/logout.html'),name='logout'),
             path('approve/<id>', views.approve, name='approve'),
             path('delete/<id>',views.comment_delete,name='comment-delete'),
             path('writepost/', views.write_post ,name='write-post')



]


# ]path('posts/<slug:slug>/', views.post_detail ,name='post-detail-page')  ,

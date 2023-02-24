from django.urls import path
from django.contrib.auth import views as auth_view
from blog import views

urlpatterns=[
             path('', views.starting_page  ,name='starting-page'),
             path('posts/', views.posts ,name='posts-page'),
             path('posts/<slug:slug>/', views.post_detail ,name='post-detail-page')  ,
             path('signup/' ,views.signup_function ,name='signup'),
             path('login/', auth_view.LoginView.as_view(template_name='blog/loginform.html') ,name='login'),






]
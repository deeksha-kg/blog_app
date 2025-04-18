from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(),name='user-posts'),#when someone goes to the blog route they will be sent to this url.py file where the remain address after cutting of /blog is used to navigate to a page further 
    path('about/',views.about,name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('post/new', PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(),name='post-delete'),
]
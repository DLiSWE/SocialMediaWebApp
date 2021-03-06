from django.urls import path
from . import views

app_name = 'Posts'
#using raw literals
urlpatterns = [
    path('', views.PostList.as_view(),name='all'),
    path('new/', views.CreatePost.as_view(),name='createpost'),
    path('by/<str:username>', views.UserPosts.as_view(),name='for_user'),
    path('by/<str:username>/<int:pk>', views.PostDetail.as_view(),name='single'),
    path('delete/<int:pk>', views.DeletePost.as_view(),name='delete'),
    path('post/<int:pk>/comment/', views.CreateComment.as_view(template_name="Posts/comment_form.html"), name='createcomment'),
]
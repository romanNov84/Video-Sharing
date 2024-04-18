from django.urls import path
from .views import CreateVideo, DetailVideo, UpdateVideo, DeleteVideo, VideoCategoryList, SearchVideo, AddLike, AddDislike, CommentDeleteView
from . import views

urlpatterns = [
    path('create/', CreateVideo.as_view(), name='video-create'),
    path('<int:pk>/', DetailVideo.as_view(), name='video-detail'),
    path('<int:pk>/update', UpdateVideo.as_view(), name='video-update'),
    path('<int:pk>/delete', DeleteVideo.as_view(), name='video-delete'),
    path('category/<int:pk>/', VideoCategoryList.as_view(), name='category-list'),
    path('search/', SearchVideo.as_view(), name='video-search'),
    path('<int:pk>/like', AddLike.as_view(), name='like'),
    path('<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    path('<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('myVideos/',  views.user_videos, name='user-videos'),
    path('about/', views.about, name='about'),
]

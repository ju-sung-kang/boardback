from django.urls import path
from . import views

urlpatterns = [
    path('post-list/', views.post_list),
    path('post-detail/<int:post_id>/', views.post_detail),
    path('post-write/', views.write_post),
    path('comment-list/<int:post_id>/', views.comment_list),
    path('comment-write/<int:post_id>/', views.write_comment),
]

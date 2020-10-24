from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('onecolumn', views.onecolumn, name='onecolumn'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]

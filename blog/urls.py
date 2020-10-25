from django.urls import path
from . import views
from django.views.static import serve
from django.urls import path, include, re_path
from mysite.settings import MEDIA_ROOT
urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.post_list, name='post_list'),
    path('twocolumn1', views.twocolumn1, name='twocolumn1'),
    path('twocolumn2', views.twocolumn2, name='twocolumn2'),
    path('onecolumn', views.onecolumn, name='onecolumn'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    re_path('media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]

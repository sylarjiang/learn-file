# _*_ coding: utf-8 _*_

from django.conf.urls import url
from bbs import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^category/(\d+)/$',views.category),
    url(r'^detail/(\d+)/$',views.article_detail,name='article_detail'),
    url(r'^post_comment/$',views.post_comment,name='post_comment'),
    url(r'^get_comments/(\d+)$',views.get_comments,name='get_comments'),
    url(r'^new_article/$',views.new_article,name='new_article'),
    url(r'^file_upload/$',views.file_upload,name='file_upload'),
    url(r'^latest_article_count/$',views.get_latest_article_count,name='get_latest_article_count'),
]
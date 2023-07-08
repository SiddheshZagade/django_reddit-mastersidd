from django.urls import re_path
from reddit import views

urlpatterns = [
    re_path(r'^$', views.frontpage, name="frontpage"),
    re_path(r'^comments/(?P<thread_id>[0-9]+)$', views.comments, name="thread"),
    re_path(r'^submission/(?P<submission_id>[0-9]+)/$', views.submission_detail, name="submission_detail"),
    re_path(r'^submit/$', views.submit, name="submit"),
    re_path(r'^post/comment/$', views.post_comment, name="post_comment"),
    re_path(r'^vote/$', views.vote, name="vote"),
    re_path(r'^submission/(?P<submission_id>[0-9]+)/edit/$', views.edit_submission, name="edit_submission"),
]

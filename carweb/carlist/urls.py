from django.conf.urls import url
from carlist import views


urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
    url(r'^post/new/$',views.CreatePostView.as_view(),name='post_new'),
    url(r'^drafts/$',views.DraftListView.as_view(),name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish')
]

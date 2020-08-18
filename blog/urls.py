from django.conf.urls import url
from . import views

#app_name = 'blog'
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),  # This is not in use but still its there for future purpose.
    url(r'^post/new/$', views.post_new, name='post_new'),                # This is not in use but still its there for future purpose.
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'), # This is not in use but still its there for future purpose.
]
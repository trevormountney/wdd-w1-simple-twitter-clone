from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

app_name = 'twitter'
urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^login$', auth_views.login, {'template_name': 'twitter/login.html'}, name='login'),
    url(r'^logout$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^post/$', views.post, name='post'),
]
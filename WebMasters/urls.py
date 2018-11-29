from django.conf.urls import url
from WebMasters import views
from django.contrib.auth import views as auth_views

# General Links

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'), #Home
]

# Login + Password Change
urlpatterns += [
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'), #Login
    url(r'^singup/$', views.signup, name='singup'),  # Sing Up
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'), #Logout
    url(r'^password_change/$', auth_views.password_change, {'template_name': 'registration/password_change.html'} , name='password_change'), #Password Change
    url(r'^password-change-done/$', auth_views.password_change_done, {'template_name': 'registration/password_change_done.html'}, name='password_change_done'), #Password Change
]
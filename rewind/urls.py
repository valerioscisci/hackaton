from django.urls import path
from rewind import views
from django.contrib.auth import views as auth_views

# General Links

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),  #Home
    path('chisiamo/', views.ChiSiamoView.as_view(), name='chisiamo'),  #Chi Siamo
    path('FAQ/', views.FAQView.as_view(), name='faq'),  #FAQ
]

# Login + Password Change
urlpatterns += [
    path('login/', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),  #Login
    path('signup/', views.signup, name='signup'),  # Sign Up
    path('logout/', auth_views.logout, {'next_page': '/'}, name='logout'),  #Logout
    path('password_change/', auth_views.password_change, {'template_name': 'registration/password_change.html'} , name='password_change'),  #Password Change
    path('password-change-done/', auth_views.password_change_done, {'template_name': 'registration/password_change_done.html'}, name='password_change_done'),  #Password Change
]
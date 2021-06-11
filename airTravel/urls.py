from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import *

urlpatterns = [
    path('', post,  name='post_info_url'),
    path('reserve/<int:id>/', index, name='reserve'),
    path('comments/<int:id>/', comments, name="comments"),
    path('profile/edit/<int:pk>/', edit),
    path('profile/delete/<int:pk>', delete),
    path('login/', user_login, name='login'),
    path('err_login/', user_login, name='err_login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile_user, name='profile'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]

from django.urls import path
from .views import index, top_sellers, register, login, advertisement_post, profile

urlpatterns = [
    path('', index, name = '/'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisement_post, name='advertisement-post'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),

]
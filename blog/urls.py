from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
   
    path('' , blog_home  , name= 'blog_home'),
    path('tag/<str:tag_name>' , blog_home , name= 'tag'),
    path('<str:cat_name>/' , blog_home , name= 'category'),
    path('author/<str:author_username>' , blog_home , name= 'author'),
    
    path('<int:pk>' , blog_single , name= 'blog_single'),    
   
    path('search/', blog_search , name= 'search'),
    
    
    
]

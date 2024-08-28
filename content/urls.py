
from django.urls import path
from . views import *

app_name = 'content'

# path (url address , view , name )

urlpatterns = [
    
    path('contact' ,contact_view , name= 'contact'),
    path('test' , test_view , name= 'test'),
    path('newsletter' , newslette_view , name= 'newsletter'),
    
]

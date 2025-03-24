from django.urls import path
from .import views
from .views import HelloWorld
from .views import Students
from .views import ContactListView

urlpatterns = [
    path('hello/', HelloWorld.as_view(), name='hello_world'),
    path('contact/', ContactListView.as_view(), name='contact_new'),
    path('students/', Students.as_view(), name='list_students'),
    path('api/contact/', views.contact_view, name='contact'),    
]


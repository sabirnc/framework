
from django.urls import path,include
from .import views

urlpatterns = [
  path('west',views.testwest,name='west'),
  path('east',views.testeast,name='east'),
]

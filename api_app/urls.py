from django.urls import path
from . import views 

urlpatterns= [
    path('studentapi/', views.studentapi,name ='studentapi'),
    path('studentapi/<int:pk>',views.studentapi,name ='studentapi'),
]
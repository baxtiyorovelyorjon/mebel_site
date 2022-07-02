from django.urls import path
from blog import views

urlpatterns = [
    path('',views.mebel,name='mebel'),
    path('about_detail/<int:pk>', views.about_detail, name='about_detail'),

]
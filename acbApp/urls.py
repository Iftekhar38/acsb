from django.urls import path, include
from acbApp import views



urlpatterns = [
    path('', views.index, name= 'index'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.feedback, name='feedback'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.login, name='login'),
    path('viewmessage/', views.viewMessage, name='viewmessage'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('compro/',  views.comPro, name='compro'),
    path('ongoingpro/', views.onGoingPro, name='ongoingpro'),
    path('delete/<id>', views.delete, name="delete")

]
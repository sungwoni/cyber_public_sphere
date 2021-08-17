
from django.urls import path

from finalapp import views

app_name = 'finalapp'

urlpatterns=[
    path('service/',views.about, name='service'),
    path('terms/', views.terms_of_use, name='terms'),
]
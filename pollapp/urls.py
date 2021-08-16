from django.urls import path

from pollapp import views

app_name='pollapp'

urlpatterns=[
    path('',views.home, name='home'),
    path('save',views.save_survey),
    path('results', views.show_result),

    # ================================================
    path('list/', views.list, name='list'),
    ]
from django.conf.urls import url
from django.contrib import admin
from mysite import views
admin.autodiscover()

urlpatterns = [

    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    url(r'^auth/register/', views.registration)

]

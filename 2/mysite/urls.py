from django.conf.urls import url
from django.contrib import admin
from mysite import views
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^materials/all/$', views.all_materials),
    url(r'^materials/get/(?P<material_id>)\d+/$', views.material_by_id)
]
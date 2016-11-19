from django.conf.urls import url, include
from django.contrib import admin
from mysite import views
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^materials/all/$', views.all_materials),
    url(r'^materials/get/(\d+)$', views.material_by_id),
    # url(r'^auth/', include('loginsys.urls')),
    url(r'^auth/register/', views.register)
]

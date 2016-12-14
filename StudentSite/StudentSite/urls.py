
from django.conf.urls import url, include
from django.contrib import admin
from mysite import views
from loginsys import log_views
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from mysite.api_views import all_materials, material_by_id
from . import settings

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^materials/all/$', views.all_materials),
    url(r'^materials/get/(\d+)/$', views.material_by_id),
    url(r'^auth/login/', log_views.login),
    url(r'^auth/logout/', log_views.logout),
    url(r'^auth/register/', log_views.register),
    url(r'^about/', views.about),
    url(r'^api/materials/all/', all_materials),
    url(r'^api/materials/get/(\d+)/$', material_by_id),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

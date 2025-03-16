from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from core import urls as core_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('painel/', include(core_urls)),
    path('', core_views.index, name='index'),
]

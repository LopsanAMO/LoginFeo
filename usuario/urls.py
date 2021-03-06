from django.conf.urls import url
from django.contrib import admin
from .views import Registro, Login, Index, Logout, ModificarDatos, Perfil
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^registro/', Registro.as_view(), name='registro'),
    url(r'^login/', Login.as_view(), name='login'),
    url(r'^index/', Index.as_view(), name='index'),
    url(r'^logout/', Logout, name='logout'),
    url(r'^modificardatos/', ModificarDatos.as_view(), name='modificar'),
    url(r'^perfil', Perfil.as_view(), name='perfil'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

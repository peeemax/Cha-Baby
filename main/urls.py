from django.contrib import admin
from django.urls import path, include
from main import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'familiarecados',views.PessoaRecadoView, 'familiarecado')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
    ]
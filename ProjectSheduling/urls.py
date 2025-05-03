"""
URL configuration for ProjectSheduling project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="SmartEcole API",
        default_version='v1',
        description="Documentation de l'API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(TokenAuthentication,),  
    
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ProjectShedulingApp.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='api-schema'), name='redoc'),
]
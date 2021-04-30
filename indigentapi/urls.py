from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Indigent API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('registry.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/',
         include('rest_auth.registration.urls')),
    path('schema/', schema_view),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

schema_view = get_swagger_view(title='API Documentation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view),
    path('api/cadastro/', include('cadastro.urls')),  # Supondo que 'cadastro.urls' é o arquivo de URLs do seu aplicativo 'cadastro'
    path('schema/', SpectacularAPIView.as_view(), name='schema'),

    # URLs para as interfaces de documentação do Swagger e ReDoc
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

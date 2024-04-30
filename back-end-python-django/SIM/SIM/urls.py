


from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

schema_view = get_swagger_view(title='API Documentation')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view),
   # path('api/', include('usuarios.urls')),  # Supondo que 'usuarios.urls' é o arquivo de URLs do seu aplicativo 'usuarios'
    path('api/usuario/', include('usuarios.urls')),  # Supondo que 'usuarios.urls' é o arquivo de URLs do seu aplicativo 'usuarios'
    path('schema/', SpectacularAPIView.as_view(), name='schema'),

    # URLs para as interfaces de documentação do Swagger e ReDoc
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # # URL para o schema de API
    # path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # # URLs para as interfaces de documentação do Swagger e ReDoc
    # path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

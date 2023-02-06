from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

swagger_view = get_schema_view(
    openapi.Info(
        title="Auth API",
        default_version='v1',
        description="auth API"
    ),
    public=True
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', swagger_view.with_ui('swagger', cache_timeout=0)),
    path('api/v1/account/', include('account.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

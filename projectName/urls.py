from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),

    #path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    #path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema"))
]

if settings.DEBUG:
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))

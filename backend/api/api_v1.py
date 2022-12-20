from configs import settings
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.conf.urls.static import static
from django.urls import include, path

from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title='AutoParkAPI',
        default_version='v1',
        description='About Cars',
        contact=openapi.Contact(email='demchyshyn.v87@gmail.com')
    ),
    public=True,
    permission_classes=(AllowAny,)
)

urlpatterns = [
    path('/cars', include('apps.cars.urls')),
    path('/auto_parks', include('apps.auto_parks.urls')),
    path('/users', include('apps.users.urls')),
    path('/auth', include('apps.auth.urls')),
    path('/doc', schema_view.with_ui('swagger', cache_timeout=0))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler400 = 'rest_framework.exceptions.bad_request'
handler500 = 'rest_framework.exceptions.server_error'

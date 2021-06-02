"""backend_stock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from rest_framework.urlpatterns import format_suffix_patterns
from drf_yasg import openapi



from api.views import get_token, get_all_users, TicketList, TicketDetail, UpdateTicketStatus, get_price_of_ticket

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('api-token-auth/', get_token.as_view()),
    path('get_users/', get_all_users.as_view(), name='get-all-user'),
    path('ticket/', TicketList.as_view(), name='Get ticket list'),
    path('update/ticket/status/', UpdateTicketStatus.as_view(), name='Get ticket list'),
    re_path(r'^ticket/(?P<pk>[0-9A-Z]+)/$', TicketDetail.as_view(), name='Get ticket details'),
    path('get_ticket_price/', get_price_of_ticket, name='Get Price'),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
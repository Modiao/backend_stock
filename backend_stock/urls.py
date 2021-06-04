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
from rest_framework_jwt.views import obtain_jwt_token



from api.views import (get_token, get_all_users, logout, get_price_of_ticket, \
        PatientAPIView, PatientRudView, TicketAPIView, TicketRudView)

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
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    path('get_users/', get_all_users.as_view(), name='get-all-user'),
    #path('auth/', get_token.as_view()),
    url(r'^auth/', obtain_jwt_token),
    path('logout/', logout),
    path('get_ticket_price/', get_price_of_ticket, name='Get Price'),
    path('patients/', PatientAPIView.as_view(), name='Patient create list'),
    path('patients/<int:id>/', PatientRudView.as_view(), name='RUD Patient'),
    path('tickets/', TicketAPIView.as_view(), name='Tikcket API lIST'),
    path('tickets/<str:id_ticket>/', TicketRudView.as_view(), name='RUD Ticket'),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
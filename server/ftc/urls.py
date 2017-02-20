"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from ftc import ftc_views
from vmail import vmail_views
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer


router = routers.DefaultRouter()
router.register(r'groups', ftc_views.GroupViewSet)
router.register(r'users', ftc_views.UserViewSet)

router.register(r'domains', vmail_views.DomainViewSet)
router.register(r'mailusers', vmail_views.MailUserViewSet)
router.register(r'aliases', vmail_views.AliasViewSet)

schema_view = get_schema_view(title='FTC API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^swagger', schema_view, name="docs"),
]


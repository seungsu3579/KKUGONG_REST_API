"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("kkugong/v1/users/", include("users.urls")),
    path("kkugong/v1/tops/", include("tops.urls")),
    path("kkugong/v1/pants/", include("pants.urls")),
    path("kkugong/v1/shoes/", include("shoes.urls")),
    path("kkugong/v1/cody/", include("cody.urls")),
    path("kkugong/v1/shop/", include("shop.urls")),
    path("kkugong/v1/scenario/", include("scenario.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

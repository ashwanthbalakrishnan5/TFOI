from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

routers = DefaultRouter()
routers.register("2019", views.Poll2019ViewSet)
routers.register("2014", views.Poll2014ViewSet)

urlpatterns = [
    path("", include(routers.urls)),
]

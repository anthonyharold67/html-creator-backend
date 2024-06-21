from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import HtmlCreatorMVS
router = DefaultRouter()
router.register("list", HtmlCreatorMVS)

urlpatterns = [
    path('', include(router.urls)),
]
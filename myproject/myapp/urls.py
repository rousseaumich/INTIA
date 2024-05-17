# urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'directions', views.DirectionViewSet)
router.register(r'succursales', views.SuccursaleViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'assurances', views.AssuranceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import ContactViewSet, UserViewSet


router = SimpleRouter()
router.register('users', UserViewSet)
router.register('', ContactViewSet)

urlpatterns = router.urls

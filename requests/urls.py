from rest_framework import routers

from requests import views

router = routers.DefaultRouter()

router.register('requests', views.UserRequestViewSet)

urlpatterns = router.urls

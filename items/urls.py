from rest_framework import routers

from items import views

router = routers.DefaultRouter()

router.register('items', views.ItemViewSet)

urlpatterns = router.urls

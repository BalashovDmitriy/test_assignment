from rest_framework import routers

from the_net.views import SupplierViewSet

router = routers.DefaultRouter()
router.register(r'suppliers', SupplierViewSet)

urlpatterns = [

]

urlpatterns += router.urls

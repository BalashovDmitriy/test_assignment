from rest_framework import routers

from the_net.views import SupplierViewSet, ProductViewSet

router = routers.DefaultRouter()

router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [

]

urlpatterns += router.urls

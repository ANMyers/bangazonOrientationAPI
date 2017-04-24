from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from bangazon.api.views import *

router = routers.DefaultRouter()
router.register(r'payment_types', PaymentTypeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product_type', ProductTypeViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'order', OrderViewSet)
router.register(r'training_program', TrainingProgramViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

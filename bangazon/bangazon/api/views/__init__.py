from bangazon.api.views.view_customer import CustomerViewSet
from bangazon.api.views.view_product import ProductViewSet
from bangazon.api.views.view_product_type import ProductTypeViewSet
from bangazon.api.views.view_order import OrderViewSet
from bangazon.api.views.view_payment_type import PaymentTypeViewSet
from bangazon.api.views.view_employee import EmployeeViewSet

__all__ = ['ProductTypeViewSet',
           'ProductViewSet', 'CustomerViewSet','OrderViewSet', 'PaymentTypeViewSet', 'EmployeeViewSet']

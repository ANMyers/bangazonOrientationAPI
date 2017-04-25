"""
bangazon api model configuration for order
"""

from django.db import models
from bangazon.api.models.model_customer import Customer


class Order(models.Model):

	"""
	This class models an order in the API's database.  

	----Fields----
	payment_type_id(decimal): Refers to PaymentType(PaymentTypeID) without a foreign key
	order_date(date): Refers to the date an order is made.
	customer_id(foreign key): Links to Customer(CustomerID) with a foreign key

	Author: Jeremy Bakker
	"""

	payment_type_id = models.DecimalField(max_digits = 20, decimal_places = 0)
	order_date = models.DateField()
	customer_id = models.ForeignKey(Customer)
"""
bangazon api model configuration for employee-computer joining tables
"""

from django.db import models
from bangazon.api.models import *


class EmployeeComputer(models.Model):
    """
    This class models the relationship between the Employee and Computer
    resources in the API's database.

    ----Fields----
    name(character): the name of the department
    budget(decimal): the budget of the department

    Author: Jeremy Bakker
    """

    date_assigned = models.DateField()
    employee_id = models.ForeignKey(Employee)
    computer_id = models.ForeignKey(Employee)


    def __str__(self):
        return self.name
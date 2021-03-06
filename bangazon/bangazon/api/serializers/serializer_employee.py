"""
bangazon api serializer configuration for employee
"""

from rest_framework import serializers
from bangazon.api.models import *


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """
    This class converts the employee model database table into Python data types.

    We exclude no fields.

    Author: Adam Myers
    """

    class Meta:
        model = Employee
        exclude = ()
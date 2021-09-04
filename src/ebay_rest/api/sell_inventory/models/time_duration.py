# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TimeDuration(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'unit': 'str',
        'value': 'int'
    }

    attribute_map = {
        'unit': 'unit',
        'value': 'value'
    }

    def __init__(self, unit=None, value=None):  # noqa: E501
        """TimeDuration - a model defined in Swagger"""  # noqa: E501
        self._unit = None
        self._value = None
        self.discriminator = None
        if unit is not None:
            self.unit = unit
        if value is not None:
            self.value = value

    @property
    def unit(self):
        """Gets the unit of this TimeDuration.  # noqa: E501

        This enumeration value indicates the time unit used to specify the fulfillment time, such as HOUR or BUSINESS_DAY. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:TimeDurationUnitEnum'>eBay API documentation</a>  # noqa: E501

        :return: The unit of this TimeDuration.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this TimeDuration.

        This enumeration value indicates the time unit used to specify the fulfillment time, such as HOUR or BUSINESS_DAY. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:TimeDurationUnitEnum'>eBay API documentation</a>  # noqa: E501

        :param unit: The unit of this TimeDuration.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def value(self):
        """Gets the value of this TimeDuration.  # noqa: E501

        The integer value in this field, along with the time unit in the unit field, will indicate the fulfillment time. For In-Store Pickup orders, this value will indicate how soon after an In-Store Pickup purchase can the buyer pick up the item at the designated store location. If the value of this field is 4, and the value of the unit field is HOUR, then the fulfillment time for the In-Store Pickup order is four hours, which means that the buyer will be able to pick up the item at the store four hours after the transaction took place. For standard orders that will be shipped, this value will indicate the expected fulfillment time if the inventory item is shipped from the inventory location. If the value of this field is 4, and the value of the unit field is BUSINESS_DAY, then the estimated delivery date after purchase is 4 business days.  # noqa: E501

        :return: The value of this TimeDuration.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TimeDuration.

        The integer value in this field, along with the time unit in the unit field, will indicate the fulfillment time. For In-Store Pickup orders, this value will indicate how soon after an In-Store Pickup purchase can the buyer pick up the item at the designated store location. If the value of this field is 4, and the value of the unit field is HOUR, then the fulfillment time for the In-Store Pickup order is four hours, which means that the buyer will be able to pick up the item at the store four hours after the transaction took place. For standard orders that will be shipped, this value will indicate the expected fulfillment time if the inventory item is shipped from the inventory location. If the value of this field is 4, and the value of the unit field is BUSINESS_DAY, then the estimated delivery date after purchase is 4 business days.  # noqa: E501

        :param value: The value of this TimeDuration.  # noqa: E501
        :type: int
        """

        self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TimeDuration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TimeDuration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

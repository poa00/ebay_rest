# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.17.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Weight(object):
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
        'value': 'float'
    }

    attribute_map = {
        'unit': 'unit',
        'value': 'value'
    }

    def __init__(self, unit=None, value=None):  # noqa: E501
        """Weight - a model defined in Swagger"""  # noqa: E501
        self._unit = None
        self._value = None
        self.discriminator = None
        if unit is not None:
            self.unit = unit
        if value is not None:
            self.value = value

    @property
    def unit(self):
        """Gets the unit of this Weight.  # noqa: E501

        The unit of measurement used to specify the weight of a shipping package. Both the <strong>unit</strong> and <strong>value</strong> fields are required if the <strong>weight</strong> container is used. If the English system of measurement is being used, the applicable values for weight units are <code>POUND</code> and <code>OUNCE</CODE>. If the metric system of measurement is being used, the applicable values for weight units are <code>KILOGRAM</code> and <code>GRAM</code>. The metric system is used by most countries outside of the US. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:WeightUnitOfMeasureEnum'>eBay API documentation</a>  # noqa: E501

        :return: The unit of this Weight.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this Weight.

        The unit of measurement used to specify the weight of a shipping package. Both the <strong>unit</strong> and <strong>value</strong> fields are required if the <strong>weight</strong> container is used. If the English system of measurement is being used, the applicable values for weight units are <code>POUND</code> and <code>OUNCE</CODE>. If the metric system of measurement is being used, the applicable values for weight units are <code>KILOGRAM</code> and <code>GRAM</code>. The metric system is used by most countries outside of the US. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:WeightUnitOfMeasureEnum'>eBay API documentation</a>  # noqa: E501

        :param unit: The unit of this Weight.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def value(self):
        """Gets the value of this Weight.  # noqa: E501

        The actual weight (in the measurement unit specified in the <strong>unit</strong> field) of the shipping package. Both the <strong>unit</strong> and <strong>value</strong> fields are required if the <strong>weight</strong> container is used. If a shipping package weighed 20.5 ounces, the container would look as follows: <br><pre>\"weight\": {<br> \"value\": 20.5,<br> \"unit\": \"OUNCE\"<br> }</pre>  # noqa: E501

        :return: The value of this Weight.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Weight.

        The actual weight (in the measurement unit specified in the <strong>unit</strong> field) of the shipping package. Both the <strong>unit</strong> and <strong>value</strong> fields are required if the <strong>weight</strong> container is used. If a shipping package weighed 20.5 ounces, the container would look as follows: <br><pre>\"weight\": {<br> \"value\": 20.5,<br> \"unit\": \"OUNCE\"<br> }</pre>  # noqa: E501

        :param value: The value of this Weight.  # noqa: E501
        :type: float
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
        if issubclass(Weight, dict):
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
        if not isinstance(other, Weight):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

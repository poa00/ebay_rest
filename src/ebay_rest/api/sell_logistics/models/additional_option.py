# coding: utf-8

"""
    Logistics API

    The <b>Logistics API</b> resources offer the following capabilities: <ul><li><b>shipping_quote</b> &ndash; Consolidates into a list a set of live shipping rates, or quotes, from which you can select a rate to ship a package.</li> <li><b>shipment</b> &ndash; Creates a \"shipment\" for the selected shipping rate.</li></ul> Call <b>createShippingQuote</b> to get a list of live shipping rates. The rates returned are all valid for a specific time window and all quoted prices are at eBay-negotiated rates. <br><br>Select one of the live rates and using its associated <b>rateId</b>, create a \"shipment\" for the package by calling <b>createFromShippingQuote</b>. Creating a shipment completes an agreement, and the cost of the base service and any added shipping options are summed into the returned <b>totalShippingCost</b> value. This action also generates a shipping label that you can use to ship the package.  The total cost of the shipment is incurred when the package is shipped using the supplied shipping label.  <p class=\"tablenote\"><b>Important!</b> Sellers must set up a payment method via their eBay account before they can use the methods in this API to create a shipment and the associated shipping label.</p>  # noqa: E501

    OpenAPI spec version: v1_beta.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AdditionalOption(object):
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
        'additional_cost': 'Amount',
        'option_type': 'str'
    }

    attribute_map = {
        'additional_cost': 'additionalCost',
        'option_type': 'optionType'
    }

    def __init__(self, additional_cost=None, option_type=None):  # noqa: E501
        """AdditionalOption - a model defined in Swagger"""  # noqa: E501
        self._additional_cost = None
        self._option_type = None
        self.discriminator = None
        if additional_cost is not None:
            self.additional_cost = additional_cost
        if option_type is not None:
            self.option_type = option_type

    @property
    def additional_cost(self):
        """Gets the additional_cost of this AdditionalOption.  # noqa: E501


        :return: The additional_cost of this AdditionalOption.  # noqa: E501
        :rtype: Amount
        """
        return self._additional_cost

    @additional_cost.setter
    def additional_cost(self, additional_cost):
        """Sets the additional_cost of this AdditionalOption.


        :param additional_cost: The additional_cost of this AdditionalOption.  # noqa: E501
        :type: Amount
        """

        self._additional_cost = additional_cost

    @property
    def option_type(self):
        """Gets the option_type of this AdditionalOption.  # noqa: E501

        The name of a shipping option that can be purchased in addition to the base shipping cost of this rate. The value supplied in this field must match exactly the option name as supplied by the selected rate.  # noqa: E501

        :return: The option_type of this AdditionalOption.  # noqa: E501
        :rtype: str
        """
        return self._option_type

    @option_type.setter
    def option_type(self, option_type):
        """Sets the option_type of this AdditionalOption.

        The name of a shipping option that can be purchased in addition to the base shipping cost of this rate. The value supplied in this field must match exactly the option name as supplied by the selected rate.  # noqa: E501

        :param option_type: The option_type of this AdditionalOption.  # noqa: E501
        :type: str
        """

        self._option_type = option_type

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
        if issubclass(AdditionalOption, dict):
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
        if not isinstance(other, AdditionalOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
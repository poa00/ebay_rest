# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (eBay business policies and seller-defined custom policies), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br/><br/>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CategoryType(object):
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
        'default': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'default': 'default',
        'name': 'name'
    }

    def __init__(self, default=None, name=None):  # noqa: E501
        """CategoryType - a model defined in Swagger"""  # noqa: E501
        self._default = None
        self._name = None
        self.discriminator = None
        if default is not None:
            self.default = default
        if name is not None:
            self.name = name

    @property
    def default(self):
        """Gets the default of this CategoryType.  # noqa: E501

        <span class=\"tablenote\"><strong>Note:</strong> This field has been deprecated and is no longer used.<ul><li>Do not include this field in any <b>create</b> or <b>update</b> method.</li><li>This field may be returned within the payload of a <b>get</b> method, but it can be ignored.</li></ul></span>  # noqa: E501

        :return: The default of this CategoryType.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this CategoryType.

        <span class=\"tablenote\"><strong>Note:</strong> This field has been deprecated and is no longer used.<ul><li>Do not include this field in any <b>create</b> or <b>update</b> method.</li><li>This field may be returned within the payload of a <b>get</b> method, but it can be ignored.</li></ul></span>  # noqa: E501

        :param default: The default of this CategoryType.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def name(self):
        """Gets the name of this CategoryType.  # noqa: E501

        The category type to which the policy applies (motor vehicles or non-motor vehicles). <br /><br />The <code>MOTORS_VEHICLES</code> category type is not valid for return policies. eBay flows do not support the return of motor vehicles. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:CategoryTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The name of this CategoryType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CategoryType.

        The category type to which the policy applies (motor vehicles or non-motor vehicles). <br /><br />The <code>MOTORS_VEHICLES</code> category type is not valid for return policies. eBay flows do not support the return of motor vehicles. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:CategoryTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param name: The name of this CategoryType.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(CategoryType, dict):
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
        if not isinstance(other, CategoryType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

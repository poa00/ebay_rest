# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (eBay business policies and seller-defined custom policies), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br/><br/>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.8.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SellingPrivileges(object):
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
        'seller_registration_completed': 'bool',
        'selling_limit': 'SellingLimit'
    }

    attribute_map = {
        'seller_registration_completed': 'sellerRegistrationCompleted',
        'selling_limit': 'sellingLimit'
    }

    def __init__(self, seller_registration_completed=None, selling_limit=None):  # noqa: E501
        """SellingPrivileges - a model defined in Swagger"""  # noqa: E501
        self._seller_registration_completed = None
        self._selling_limit = None
        self.discriminator = None
        if seller_registration_completed is not None:
            self.seller_registration_completed = seller_registration_completed
        if selling_limit is not None:
            self.selling_limit = selling_limit

    @property
    def seller_registration_completed(self):
        """Gets the seller_registration_completed of this SellingPrivileges.  # noqa: E501

        If this field is returned as <code>true</code>, the seller's registration is completed. If this field is returned as <code>false</code>, the registration process is not complete.  # noqa: E501

        :return: The seller_registration_completed of this SellingPrivileges.  # noqa: E501
        :rtype: bool
        """
        return self._seller_registration_completed

    @seller_registration_completed.setter
    def seller_registration_completed(self, seller_registration_completed):
        """Sets the seller_registration_completed of this SellingPrivileges.

        If this field is returned as <code>true</code>, the seller's registration is completed. If this field is returned as <code>false</code>, the registration process is not complete.  # noqa: E501

        :param seller_registration_completed: The seller_registration_completed of this SellingPrivileges.  # noqa: E501
        :type: bool
        """

        self._seller_registration_completed = seller_registration_completed

    @property
    def selling_limit(self):
        """Gets the selling_limit of this SellingPrivileges.  # noqa: E501


        :return: The selling_limit of this SellingPrivileges.  # noqa: E501
        :rtype: SellingLimit
        """
        return self._selling_limit

    @selling_limit.setter
    def selling_limit(self, selling_limit):
        """Sets the selling_limit of this SellingPrivileges.


        :param selling_limit: The selling_limit of this SellingPrivileges.  # noqa: E501
        :type: SellingLimit
        """

        self._selling_limit = selling_limit

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
        if issubclass(SellingPrivileges, dict):
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
        if not isinstance(other, SellingPrivileges):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

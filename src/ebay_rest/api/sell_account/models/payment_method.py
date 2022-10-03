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

class PaymentMethod(object):
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
        'brands': 'list[str]',
        'payment_method_type': 'str',
        'recipient_account_reference': 'RecipientAccountReference'
    }

    attribute_map = {
        'brands': 'brands',
        'payment_method_type': 'paymentMethodType',
        'recipient_account_reference': 'recipientAccountReference'
    }

    def __init__(self, brands=None, payment_method_type=None, recipient_account_reference=None):  # noqa: E501
        """PaymentMethod - a model defined in Swagger"""  # noqa: E501
        self._brands = None
        self._payment_method_type = None
        self._recipient_account_reference = None
        self.discriminator = None
        if brands is not None:
            self.brands = brands
        if payment_method_type is not None:
            self.payment_method_type = payment_method_type
        if recipient_account_reference is not None:
            self.recipient_account_reference = recipient_account_reference

    @property
    def brands(self):
        """Gets the brands of this PaymentMethod.  # noqa: E501

        <span class=\"tablenote\"><b>Note</b>: This array is no longer applicable and should not be used. eBay now controls all electronic payment methods available for a marketplace, and a seller never has to specify any electronic payment methods, including any credit card brands accepted. </span>  # noqa: E501

        :return: The brands of this PaymentMethod.  # noqa: E501
        :rtype: list[str]
        """
        return self._brands

    @brands.setter
    def brands(self, brands):
        """Sets the brands of this PaymentMethod.

        <span class=\"tablenote\"><b>Note</b>: This array is no longer applicable and should not be used. eBay now controls all electronic payment methods available for a marketplace, and a seller never has to specify any electronic payment methods, including any credit card brands accepted. </span>  # noqa: E501

        :param brands: The brands of this PaymentMethod.  # noqa: E501
        :type: list[str]
        """

        self._brands = brands

    @property
    def payment_method_type(self):
        """Gets the payment_method_type of this PaymentMethod.  # noqa: E501

        eBay now controls all electronic payment methods available for a marketplace, so only offline payment method enum values may be used in this field, and offline payment methods will only be applicable to listings that require or support offline payments. See the <b>PaymentMethodTypeEnum</b> type for supported offline payment method enum values. </p> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:PaymentMethodTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The payment_method_type of this PaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_type

    @payment_method_type.setter
    def payment_method_type(self, payment_method_type):
        """Sets the payment_method_type of this PaymentMethod.

        eBay now controls all electronic payment methods available for a marketplace, so only offline payment method enum values may be used in this field, and offline payment methods will only be applicable to listings that require or support offline payments. See the <b>PaymentMethodTypeEnum</b> type for supported offline payment method enum values. </p> For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/account/types/api:PaymentMethodTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param payment_method_type: The payment_method_type of this PaymentMethod.  # noqa: E501
        :type: str
        """

        self._payment_method_type = payment_method_type

    @property
    def recipient_account_reference(self):
        """Gets the recipient_account_reference of this PaymentMethod.  # noqa: E501


        :return: The recipient_account_reference of this PaymentMethod.  # noqa: E501
        :rtype: RecipientAccountReference
        """
        return self._recipient_account_reference

    @recipient_account_reference.setter
    def recipient_account_reference(self, recipient_account_reference):
        """Sets the recipient_account_reference of this PaymentMethod.


        :param recipient_account_reference: The recipient_account_reference of this PaymentMethod.  # noqa: E501
        :type: RecipientAccountReference
        """

        self._recipient_account_reference = recipient_account_reference

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
        if issubclass(PaymentMethod, dict):
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
        if not isinstance(other, PaymentMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

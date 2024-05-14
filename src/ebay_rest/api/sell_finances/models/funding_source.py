# coding: utf-8

"""
    eBay Finances API

    This API is used to retrieve seller payouts and monetary transaction details related to those payouts.  # noqa: E501

    OpenAPI spec version: v1.17.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FundingSource(object):
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
        'brand': 'str',
        'memo': 'str',
        'type': 'str'
    }

    attribute_map = {
        'brand': 'brand',
        'memo': 'memo',
        'type': 'type'
    }

    def __init__(self, brand=None, memo=None, type=None):  # noqa: E501
        """FundingSource - a model defined in Swagger"""  # noqa: E501
        self._brand = None
        self._memo = None
        self._type = None
        self.discriminator = None
        if brand is not None:
            self.brand = brand
        if memo is not None:
            self.memo = memo
        if type is not None:
            self.type = type

    @property
    def brand(self):
        """Gets the brand of this FundingSource.  # noqa: E501

        The brand name of the credit card or the name of the financial institution that is the source of payment. This field may not be populated for other funding sources.  # noqa: E501

        :return: The brand of this FundingSource.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this FundingSource.

        The brand name of the credit card or the name of the financial institution that is the source of payment. This field may not be populated for other funding sources.  # noqa: E501

        :param brand: The brand of this FundingSource.  # noqa: E501
        :type: str
        """

        self._brand = brand

    @property
    def memo(self):
        """Gets the memo of this FundingSource.  # noqa: E501

        This field provides a note about the funding source. If the seller's credit card or bank account is the funding source, this field might contain the last four digits of the credit card or bank account. This field may also be returned as null.  # noqa: E501

        :return: The memo of this FundingSource.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this FundingSource.

        This field provides a note about the funding source. If the seller's credit card or bank account is the funding source, this field might contain the last four digits of the credit card or bank account. This field may also be returned as null.  # noqa: E501

        :param memo: The memo of this FundingSource.  # noqa: E501
        :type: str
        """

        self._memo = memo

    @property
    def type(self):
        """Gets the type of this FundingSource.  # noqa: E501

        The string value returned here indicates the funding source. Possible values include the following:<ul><li><code>AVAILABLE_FUNDS</code>: transfer is funded with seller payout funds</li><li><code>CREDIT_CARD</code>: transfer is funded with seller's credit card</li><li><code>BANK</code>: transfer is funded with a direct debit to seller's bank account on file with eBay</li><li><code>PAY_UPON_INVOICE</code>: eBay will bill the seller for the transfer on the monthly invoice</li></ul>  # noqa: E501

        :return: The type of this FundingSource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FundingSource.

        The string value returned here indicates the funding source. Possible values include the following:<ul><li><code>AVAILABLE_FUNDS</code>: transfer is funded with seller payout funds</li><li><code>CREDIT_CARD</code>: transfer is funded with seller's credit card</li><li><code>BANK</code>: transfer is funded with a direct debit to seller's bank account on file with eBay</li><li><code>PAY_UPON_INVOICE</code>: eBay will bill the seller for the transfer on the monthly invoice</li></ul>  # noqa: E501

        :param type: The type of this FundingSource.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(FundingSource, dict):
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
        if not isinstance(other, FundingSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

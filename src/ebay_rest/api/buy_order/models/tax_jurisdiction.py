# coding: utf-8

"""
    Order API

    <span class=\"tablenote\"><b>Note:</b> The Order API (v2) currently only supports the guest payment/checkout flow. If you need to support member payment/checkout flow, use the <a href=\"/api-docs/buy/order_v1/resources/methods\">v1_beta version</a> of the Order API.</span><br><br><span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"><img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\"  alt=\"Limited Release\" title=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br><br>The Order API provides interfaces that let shoppers pay for items. It also returns payment and shipping status of the order.  # noqa: E501

    OpenAPI spec version: v2.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TaxJurisdiction(object):
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
        'region': 'Region',
        'tax_jurisdiction_id': 'str'
    }

    attribute_map = {
        'region': 'region',
        'tax_jurisdiction_id': 'taxJurisdictionId'
    }

    def __init__(self, region=None, tax_jurisdiction_id=None):  # noqa: E501
        """TaxJurisdiction - a model defined in Swagger"""  # noqa: E501
        self._region = None
        self._tax_jurisdiction_id = None
        self.discriminator = None
        if region is not None:
            self.region = region
        if tax_jurisdiction_id is not None:
            self.tax_jurisdiction_id = tax_jurisdiction_id

    @property
    def region(self):
        """Gets the region of this TaxJurisdiction.  # noqa: E501


        :return: The region of this TaxJurisdiction.  # noqa: E501
        :rtype: Region
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this TaxJurisdiction.


        :param region: The region of this TaxJurisdiction.  # noqa: E501
        :type: Region
        """

        self._region = region

    @property
    def tax_jurisdiction_id(self):
        """Gets the tax_jurisdiction_id of this TaxJurisdiction.  # noqa: E501

        The identifier of the tax jurisdiction.  # noqa: E501

        :return: The tax_jurisdiction_id of this TaxJurisdiction.  # noqa: E501
        :rtype: str
        """
        return self._tax_jurisdiction_id

    @tax_jurisdiction_id.setter
    def tax_jurisdiction_id(self, tax_jurisdiction_id):
        """Sets the tax_jurisdiction_id of this TaxJurisdiction.

        The identifier of the tax jurisdiction.  # noqa: E501

        :param tax_jurisdiction_id: The tax_jurisdiction_id of this TaxJurisdiction.  # noqa: E501
        :type: str
        """

        self._tax_jurisdiction_id = tax_jurisdiction_id

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
        if issubclass(TaxJurisdiction, dict):
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
        if not isinstance(other, TaxJurisdiction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

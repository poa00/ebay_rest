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

class FeesSummaryResponse(object):
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
        'fee_summaries': 'list[FeeSummary]'
    }

    attribute_map = {
        'fee_summaries': 'feeSummaries'
    }

    def __init__(self, fee_summaries=None):  # noqa: E501
        """FeesSummaryResponse - a model defined in Swagger"""  # noqa: E501
        self._fee_summaries = None
        self.discriminator = None
        if fee_summaries is not None:
            self.fee_summaries = fee_summaries

    @property
    def fee_summaries(self):
        """Gets the fee_summaries of this FeesSummaryResponse.  # noqa: E501

        This container consists of an array of one or more listing fees that the seller can expect to pay for unpublished offers specified in the call request. Many fee types will get returned even when they are 0.0.  # noqa: E501

        :return: The fee_summaries of this FeesSummaryResponse.  # noqa: E501
        :rtype: list[FeeSummary]
        """
        return self._fee_summaries

    @fee_summaries.setter
    def fee_summaries(self, fee_summaries):
        """Sets the fee_summaries of this FeesSummaryResponse.

        This container consists of an array of one or more listing fees that the seller can expect to pay for unpublished offers specified in the call request. Many fee types will get returned even when they are 0.0.  # noqa: E501

        :param fee_summaries: The fee_summaries of this FeesSummaryResponse.  # noqa: E501
        :type: list[FeeSummary]
        """

        self._fee_summaries = fee_summaries

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
        if issubclass(FeesSummaryResponse, dict):
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
        if not isinstance(other, FeesSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

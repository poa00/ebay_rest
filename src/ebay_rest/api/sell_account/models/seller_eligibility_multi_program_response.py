# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (eBay business policies and seller-defined custom policies), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br><br>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.9.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SellerEligibilityMultiProgramResponse(object):
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
        'advertising_eligibility': 'list[SellerEligibilityResponse]'
    }

    attribute_map = {
        'advertising_eligibility': 'advertisingEligibility'
    }

    def __init__(self, advertising_eligibility=None):  # noqa: E501
        """SellerEligibilityMultiProgramResponse - a model defined in Swagger"""  # noqa: E501
        self._advertising_eligibility = None
        self.discriminator = None
        if advertising_eligibility is not None:
            self.advertising_eligibility = advertising_eligibility

    @property
    def advertising_eligibility(self):
        """Gets the advertising_eligibility of this SellerEligibilityMultiProgramResponse.  # noqa: E501

        An array of response fields that define the seller eligibility for eBay advertising programs.  # noqa: E501

        :return: The advertising_eligibility of this SellerEligibilityMultiProgramResponse.  # noqa: E501
        :rtype: list[SellerEligibilityResponse]
        """
        return self._advertising_eligibility

    @advertising_eligibility.setter
    def advertising_eligibility(self, advertising_eligibility):
        """Sets the advertising_eligibility of this SellerEligibilityMultiProgramResponse.

        An array of response fields that define the seller eligibility for eBay advertising programs.  # noqa: E501

        :param advertising_eligibility: The advertising_eligibility of this SellerEligibilityMultiProgramResponse.  # noqa: E501
        :type: list[SellerEligibilityResponse]
        """

        self._advertising_eligibility = advertising_eligibility

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
        if issubclass(SellerEligibilityMultiProgramResponse, dict):
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
        if not isinstance(other, SellerEligibilityMultiProgramResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

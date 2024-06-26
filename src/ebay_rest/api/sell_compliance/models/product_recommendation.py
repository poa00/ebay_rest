# coding: utf-8

"""
    Compliance API

    Service for providing information to sellers about their listings being non-compliant, or at risk for becoming non-compliant, against eBay listing policies.  # noqa: E501

    OpenAPI spec version: 1.4.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ProductRecommendation(object):
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
        'epid': 'str'
    }

    attribute_map = {
        'epid': 'epid'
    }

    def __init__(self, epid=None):  # noqa: E501
        """ProductRecommendation - a model defined in Swagger"""  # noqa: E501
        self._epid = None
        self.discriminator = None
        if epid is not None:
            self.epid = epid

    @property
    def epid(self):
        """Gets the epid of this ProductRecommendation.  # noqa: E501

        This field will return the eBay Product ID {ePID) of an eBay Catalog product that eBay recommends that the seller use to make their listing compliant. <br><br><span class=\"tablenote\"><strong>Note:</strong> Product Adoption is not enforced at this time. Product Adoption violations are no longer returned.</span>  # noqa: E501

        :return: The epid of this ProductRecommendation.  # noqa: E501
        :rtype: str
        """
        return self._epid

    @epid.setter
    def epid(self, epid):
        """Sets the epid of this ProductRecommendation.

        This field will return the eBay Product ID {ePID) of an eBay Catalog product that eBay recommends that the seller use to make their listing compliant. <br><br><span class=\"tablenote\"><strong>Note:</strong> Product Adoption is not enforced at this time. Product Adoption violations are no longer returned.</span>  # noqa: E501

        :param epid: The epid of this ProductRecommendation.  # noqa: E501
        :type: str
        """

        self._epid = epid

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
        if issubclass(ProductRecommendation, dict):
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
        if not isinstance(other, ProductRecommendation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

"""
    Compliance API

    Service for providing information to sellers about their listings being non-compliant, or at risk for becoming non-compliant, against eBay listing policies.  # noqa: E501

    OpenAPI spec version: 1.4.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class VariationDetails(object):
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
        'sku': 'str',
        'variation_aspects': 'list[NameValueList]'
    }

    attribute_map = {
        'sku': 'sku',
        'variation_aspects': 'variationAspects'
    }

    def __init__(self, sku=None, variation_aspects=None):  # noqa: E501
        """VariationDetails - a model defined in Swagger"""  # noqa: E501
        self._sku = None
        self._variation_aspects = None
        self.discriminator = None
        if sku is not None:
            self.sku = sku
        if variation_aspects is not None:
            self.variation_aspects = variation_aspects

    @property
    def sku(self):
        """Gets the sku of this VariationDetails.  # noqa: E501

        The seller-defined SKU value of the variation within the multiple-variation listing with the violation{s). This field is only returned if a seller-defined SKU value is defined for the variation. SKU values are optional in listing except when creating listings using the Inventory API.  # noqa: E501

        :return: The sku of this VariationDetails.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this VariationDetails.

        The seller-defined SKU value of the variation within the multiple-variation listing with the violation{s). This field is only returned if a seller-defined SKU value is defined for the variation. SKU values are optional in listing except when creating listings using the Inventory API.  # noqa: E501

        :param sku: The sku of this VariationDetails.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def variation_aspects(self):
        """Gets the variation_aspects of this VariationDetails.  # noqa: E501

        An array of one or more variation aspects that define a variation within a multiple-variation listing. The aspect{s) returned here define the individual variation, because these aspects will differ for each variation. Common varying aspects include color and size.  # noqa: E501

        :return: The variation_aspects of this VariationDetails.  # noqa: E501
        :rtype: list[NameValueList]
        """
        return self._variation_aspects

    @variation_aspects.setter
    def variation_aspects(self, variation_aspects):
        """Sets the variation_aspects of this VariationDetails.

        An array of one or more variation aspects that define a variation within a multiple-variation listing. The aspect{s) returned here define the individual variation, because these aspects will differ for each variation. Common varying aspects include color and size.  # noqa: E501

        :param variation_aspects: The variation_aspects of this VariationDetails.  # noqa: E501
        :type: list[NameValueList]
        """

        self._variation_aspects = variation_aspects

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
        if issubclass(VariationDetails, dict):
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
        if not isinstance(other, VariationDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

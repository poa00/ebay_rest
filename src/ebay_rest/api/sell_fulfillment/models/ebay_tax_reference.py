# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.19.18
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EbayTaxReference(object):
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
        'name': 'str',
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value'
    }

    def __init__(self, name=None, value=None):  # noqa: E501
        """EbayTaxReference - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._value = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value

    @property
    def name(self):
        """Gets the name of this EbayTaxReference.  # noqa: E501

        This field value is returned to indicate the VAT tax type, which will vary by country/region. This string value will be one of the following:<ul><li><code>ABN</code>: if this string is returned, the ID in the <strong>value</strong> field is an Australia tax ID</li><li><code>DDG</code>: if this string is returned, it indicates that tax has been collected and remitted for Digitally Delivered Goods (DDG)</li><li><code>IOSS</code>: if this string is returned, the ID in the <strong>value</strong> field is an eBay EU or UK IOSS number</li><li><code>IRD</code>: if this string is returned, the ID in the <strong>value</strong> field is an eBay New Zealand tax ID</li><li><code>OSS</code>: if this string is returned, the ID in the <strong>value</strong> field is an  eBay Germany VAT ID</li><li><code>VOEC</code>: if this string is returned, the ID in the <strong>value</strong> field is an eBay Norway tax ID</li></ul>  # noqa: E501

        :return: The name of this EbayTaxReference.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EbayTaxReference.

        This field value is returned to indicate the VAT tax type, which will vary by country/region. This string value will be one of the following:<ul><li><code>ABN</code>: if this string is returned, the ID in the <strong>value</strong> field is an Australia tax ID</li><li><code>DDG</code>: if this string is returned, it indicates that tax has been collected and remitted for Digitally Delivered Goods (DDG)</li><li><code>IOSS</code>: if this string is returned, the ID in the <strong>value</strong> field is an eBay EU or UK IOSS number</li><li><code>IRD</code>: if this string is returned, the ID in the <strong>value</strong> field is an eBay New Zealand tax ID</li><li><code>OSS</code>: if this string is returned, the ID in the <strong>value</strong> field is an  eBay Germany VAT ID</li><li><code>VOEC</code>: if this string is returned, the ID in the <strong>value</strong> field is an eBay Norway tax ID</li></ul>  # noqa: E501

        :param name: The name of this EbayTaxReference.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this EbayTaxReference.  # noqa: E501

        The value returned in this field is the VAT identifier number (VATIN), which will vary by country/region. This field will be returned if VAT tax is applicable for the order. The <strong>name</strong> field indicates the VAT tax type, which will vary by country/region: <ul><li><strong>ABN</strong>: <em>eBay AU tax ID</em></li><li><strong>IOSS</strong>: <em>eBay EU IOSS number</em> / <em>eBay UK IOSS number</em></li><li><strong>IRD</strong>: <em>eBay NZ tax ID</em></li><li><strong>OSS</strong>: <em>eBay DE VAT ID</em></li><li><strong>VOEC</strong>: <em>eBay NO number</em></li></ul>  # noqa: E501

        :return: The value of this EbayTaxReference.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this EbayTaxReference.

        The value returned in this field is the VAT identifier number (VATIN), which will vary by country/region. This field will be returned if VAT tax is applicable for the order. The <strong>name</strong> field indicates the VAT tax type, which will vary by country/region: <ul><li><strong>ABN</strong>: <em>eBay AU tax ID</em></li><li><strong>IOSS</strong>: <em>eBay EU IOSS number</em> / <em>eBay UK IOSS number</em></li><li><strong>IRD</strong>: <em>eBay NZ tax ID</em></li><li><strong>OSS</strong>: <em>eBay DE VAT ID</em></li><li><strong>VOEC</strong>: <em>eBay NO number</em></li></ul>  # noqa: E501

        :param value: The value of this EbayTaxReference.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if issubclass(EbayTaxReference, dict):
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
        if not isinstance(other, EbayTaxReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

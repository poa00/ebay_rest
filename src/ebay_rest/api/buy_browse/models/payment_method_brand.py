# coding: utf-8

"""
    Browse API

    <p>The Browse API has the following resources:</p>   <ul> <li><b> item_summary: </b> Lets shoppers search for specific items by keyword, GTIN, category, charity, product, image </b><a href=\"/api-docs/static/versioning.html#experimental \" target=\"_blank\"><img src=\"/cms/img/docs/experimental-icon.svg\" class=\"legend-icon experimental-icon\" alt=\"Experimental Method\" title=\"Experimental Method\" />(Experimental Method)</a>, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values, or UI parameters.</li>   <li><b> item: </b> <ul><li>Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part.</li> <li>Provides a bridge between the eBay legacy APIs, such as <b> Finding</b>, and the RESTful APIs, which use different formats for the item IDs.</li>  </ul> </li>  </ul>       <p>The <b> item_summary</b>, <b> search_by_image</b>, and <b> item</b> resource calls require an <a href=\"/api-docs/static/oauth-client-credentials-grant.html\">Application access token</a>.</p>  # noqa: E501

    OpenAPI spec version: v1.19.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PaymentMethodBrand(object):
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
        'payment_method_brand_type': 'str',
        'logo_image': 'Image'
    }

    attribute_map = {
        'payment_method_brand_type': 'paymentMethodBrandType',
        'logo_image': 'logoImage'
    }

    def __init__(self, payment_method_brand_type=None, logo_image=None):  # noqa: E501
        """PaymentMethodBrand - a model defined in Swagger"""  # noqa: E501
        self._payment_method_brand_type = None
        self._logo_image = None
        self.discriminator = None
        if payment_method_brand_type is not None:
            self.payment_method_brand_type = payment_method_brand_type
        if logo_image is not None:
            self.logo_image = logo_image

    @property
    def payment_method_brand_type(self):
        """Gets the payment_method_brand_type of this PaymentMethodBrand.  # noqa: E501

        The payment method brand, such as Visa or PayPal. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:PaymentMethodBrandEnum'>eBay API documentation</a>  # noqa: E501

        :return: The payment_method_brand_type of this PaymentMethodBrand.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_brand_type

    @payment_method_brand_type.setter
    def payment_method_brand_type(self, payment_method_brand_type):
        """Sets the payment_method_brand_type of this PaymentMethodBrand.

        The payment method brand, such as Visa or PayPal. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:PaymentMethodBrandEnum'>eBay API documentation</a>  # noqa: E501

        :param payment_method_brand_type: The payment_method_brand_type of this PaymentMethodBrand.  # noqa: E501
        :type: str
        """

        self._payment_method_brand_type = payment_method_brand_type

    @property
    def logo_image(self):
        """Gets the logo_image of this PaymentMethodBrand.  # noqa: E501


        :return: The logo_image of this PaymentMethodBrand.  # noqa: E501
        :rtype: Image
        """
        return self._logo_image

    @logo_image.setter
    def logo_image(self, logo_image):
        """Sets the logo_image of this PaymentMethodBrand.


        :param logo_image: The logo_image of this PaymentMethodBrand.  # noqa: E501
        :type: Image
        """

        self._logo_image = logo_image

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
        if issubclass(PaymentMethodBrand, dict):
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
        if not isinstance(other, PaymentMethodBrand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

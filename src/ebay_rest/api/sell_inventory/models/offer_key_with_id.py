# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.16.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OfferKeyWithId(object):
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
        'offer_id': 'str'
    }

    attribute_map = {
        'offer_id': 'offerId'
    }

    def __init__(self, offer_id=None):  # noqa: E501
        """OfferKeyWithId - a model defined in Swagger"""  # noqa: E501
        self._offer_id = None
        self.discriminator = None
        if offer_id is not None:
            self.offer_id = offer_id

    @property
    def offer_id(self):
        """Gets the offer_id of this OfferKeyWithId.  # noqa: E501

        The unique identifier of an unpublished offer for which expected listing fees will be retrieved. One to 250 <strong>offerId</strong> values can be passed in to the <strong>offers</strong> container for one <strong>getListingFees</strong> call. Errors will occur if <strong>offerId</strong> values representing published offers are passed in.  # noqa: E501

        :return: The offer_id of this OfferKeyWithId.  # noqa: E501
        :rtype: str
        """
        return self._offer_id

    @offer_id.setter
    def offer_id(self, offer_id):
        """Sets the offer_id of this OfferKeyWithId.

        The unique identifier of an unpublished offer for which expected listing fees will be retrieved. One to 250 <strong>offerId</strong> values can be passed in to the <strong>offers</strong> container for one <strong>getListingFees</strong> call. Errors will occur if <strong>offerId</strong> values representing published offers are passed in.  # noqa: E501

        :param offer_id: The offer_id of this OfferKeyWithId.  # noqa: E501
        :type: str
        """

        self._offer_id = offer_id

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
        if issubclass(OfferKeyWithId, dict):
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
        if not isinstance(other, OfferKeyWithId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

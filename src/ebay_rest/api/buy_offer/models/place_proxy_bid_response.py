# coding: utf-8

"""
    Buy Offer API

    <span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units. For information on how to obtain access to this API in production, see the <a href=\"/../api-docs/buy/static/buy-requirements.html\" target=\"_blank\">Buy APIs Requirements</a>.</span><br><br>The Buy Offer API enables Partners to place proxy bids for a buyer and retrieve the auctions where the buyer is bidding.  By placing a proxy bid, the buyer is agreeing to purchase the item if they win the auction.  # noqa: E501

    OpenAPI spec version: v1_beta.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PlaceProxyBidResponse(object):
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
        'proxy_bid_id': 'str'
    }

    attribute_map = {
        'proxy_bid_id': 'proxyBidId'
    }

    def __init__(self, proxy_bid_id=None):  # noqa: E501
        """PlaceProxyBidResponse - a model defined in Swagger"""  # noqa: E501
        self._proxy_bid_id = None
        self.discriminator = None
        if proxy_bid_id is not None:
            self.proxy_bid_id = proxy_bid_id

    @property
    def proxy_bid_id(self):
        """Gets the proxy_bid_id of this PlaceProxyBidResponse.  # noqa: E501

        Identifier of the proxy bid created by the request. This indicates that the bid was placed and is not used for anything else.  # noqa: E501

        :return: The proxy_bid_id of this PlaceProxyBidResponse.  # noqa: E501
        :rtype: str
        """
        return self._proxy_bid_id

    @proxy_bid_id.setter
    def proxy_bid_id(self, proxy_bid_id):
        """Sets the proxy_bid_id of this PlaceProxyBidResponse.

        Identifier of the proxy bid created by the request. This indicates that the bid was placed and is not used for anything else.  # noqa: E501

        :param proxy_bid_id: The proxy_bid_id of this PlaceProxyBidResponse.  # noqa: E501
        :type: str
        """

        self._proxy_bid_id = proxy_bid_id

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
        if issubclass(PlaceProxyBidResponse, dict):
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
        if not isinstance(other, PlaceProxyBidResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

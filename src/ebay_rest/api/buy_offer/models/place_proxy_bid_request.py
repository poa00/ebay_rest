# coding: utf-8

"""
    Buy Offer API

    <span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units.</span><br /><br />The Buy Offer API enables Partners to place proxy bids for a buyer and retrieve the auctions where the buyer is bidding.  By placing a proxy bid, the buyer is agreeing to purchase the item if they win the auction. </p>   # noqa: E501

    OpenAPI spec version: v1_beta.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PlaceProxyBidRequest(object):
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
        'max_amount': 'Amount',
        'user_consent': 'UserConsent'
    }

    attribute_map = {
        'max_amount': 'maxAmount',
        'user_consent': 'userConsent'
    }

    def __init__(self, max_amount=None, user_consent=None):  # noqa: E501
        """PlaceProxyBidRequest - a model defined in Swagger"""  # noqa: E501
        self._max_amount = None
        self._user_consent = None
        self.discriminator = None
        if max_amount is not None:
            self.max_amount = max_amount
        if user_consent is not None:
            self.user_consent = user_consent

    @property
    def max_amount(self):
        """Gets the max_amount of this PlaceProxyBidRequest.  # noqa: E501


        :return: The max_amount of this PlaceProxyBidRequest.  # noqa: E501
        :rtype: Amount
        """
        return self._max_amount

    @max_amount.setter
    def max_amount(self, max_amount):
        """Sets the max_amount of this PlaceProxyBidRequest.


        :param max_amount: The max_amount of this PlaceProxyBidRequest.  # noqa: E501
        :type: Amount
        """

        self._max_amount = max_amount

    @property
    def user_consent(self):
        """Gets the user_consent of this PlaceProxyBidRequest.  # noqa: E501


        :return: The user_consent of this PlaceProxyBidRequest.  # noqa: E501
        :rtype: UserConsent
        """
        return self._user_consent

    @user_consent.setter
    def user_consent(self, user_consent):
        """Sets the user_consent of this PlaceProxyBidRequest.


        :param user_consent: The user_consent of this PlaceProxyBidRequest.  # noqa: E501
        :type: UserConsent
        """

        self._user_consent = user_consent

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
        if issubclass(PlaceProxyBidRequest, dict):
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
        if not isinstance(other, PlaceProxyBidRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

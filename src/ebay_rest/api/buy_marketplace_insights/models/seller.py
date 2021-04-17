# coding: utf-8

"""
    Marketplace Insights API

    <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#Limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> The Marketplace Insights API provides the ability to search for sold items on eBay by keyword, GTIN, category, and product and returns the of sales history of those items.  # noqa: E501

    OpenAPI spec version: v1_beta.2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Seller(object):
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
        'feedback_percentage': 'str',
        'feedback_score': 'int',
        'username': 'str'
    }

    attribute_map = {
        'feedback_percentage': 'feedbackPercentage',
        'feedback_score': 'feedbackScore',
        'username': 'username'
    }

    def __init__(self, feedback_percentage=None, feedback_score=None, username=None):  # noqa: E501
        """Seller - a model defined in Swagger"""  # noqa: E501
        self._feedback_percentage = None
        self._feedback_score = None
        self._username = None
        self.discriminator = None
        if feedback_percentage is not None:
            self.feedback_percentage = feedback_percentage
        if feedback_score is not None:
            self.feedback_score = feedback_score
        if username is not None:
            self.username = username

    @property
    def feedback_percentage(self):
        """Gets the feedback_percentage of this Seller.  # noqa: E501

        The percentage of the total positive feedback.  # noqa: E501

        :return: The feedback_percentage of this Seller.  # noqa: E501
        :rtype: str
        """
        return self._feedback_percentage

    @feedback_percentage.setter
    def feedback_percentage(self, feedback_percentage):
        """Sets the feedback_percentage of this Seller.

        The percentage of the total positive feedback.  # noqa: E501

        :param feedback_percentage: The feedback_percentage of this Seller.  # noqa: E501
        :type: str
        """

        self._feedback_percentage = feedback_percentage

    @property
    def feedback_score(self):
        """Gets the feedback_score of this Seller.  # noqa: E501

        The feedback score of the seller. This value is based on the ratings from eBay members that bought items from this seller.  # noqa: E501

        :return: The feedback_score of this Seller.  # noqa: E501
        :rtype: int
        """
        return self._feedback_score

    @feedback_score.setter
    def feedback_score(self, feedback_score):
        """Sets the feedback_score of this Seller.

        The feedback score of the seller. This value is based on the ratings from eBay members that bought items from this seller.  # noqa: E501

        :param feedback_score: The feedback_score of this Seller.  # noqa: E501
        :type: int
        """

        self._feedback_score = feedback_score

    @property
    def username(self):
        """Gets the username of this Seller.  # noqa: E501

        The username created by the seller for use on eBay.  # noqa: E501

        :return: The username of this Seller.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Seller.

        The username created by the seller for use on eBay.  # noqa: E501

        :param username: The username of this Seller.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(Seller, dict):
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
        if not isinstance(other, Seller):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
